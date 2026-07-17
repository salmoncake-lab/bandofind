from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from database.supabase import supabase
import uuid


router = APIRouter()


@router.post("/report")
async def create_report(

    anime_name: str = Form(...),

    character_name: str = Form(...),

    product_name: str = Form(...),

    store_name: str = Form(...),

    price: int = Form(...),

    image: UploadFile = File(...)

):

    try:

        # 檢查圖片格式
        if not image.content_type.startswith("image/"):
            raise HTTPException(
                status_code=400,
                detail="只能上傳圖片"
            )


        # 建立唯一檔名
        filename = (
            f"{uuid.uuid4()}-{image.filename}"
        )


        # 讀取圖片
        file_content = await image.read()


        # 上傳 Supabase Storage
        supabase.storage \
            .from_("reports") \
            .upload(
                filename,
                file_content,
                {
                    "content-type": image.content_type
                }
            )


        # 取得公開網址
        image_url = (
            supabase
            .storage
            .from_("reports")
            .get_public_url(filename)
        )


        # 寫入 Report Table
        result = (
            supabase
            .table("report")
            .insert({

                "anime_name": anime_name,

                "character_name": character_name,

                "product_name": product_name,

                "store_name": store_name,

                "price": price,

                "image_url": image_url,

                "message":
                "User submitted report"

            })
            .execute()
        )


        return {

            "message":
            "Report created successfully",

            "image_url":
            image_url,

            "data":
            result.data

        }


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )
