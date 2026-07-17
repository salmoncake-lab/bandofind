from fastapi import APIRouter
from database.supabase import supabase


router = APIRouter()



@router.get("/search")
def search_character(name:str):


    result = (

        supabase

        .table("character")

        .select(

        """
        id,
        name,

        anime(
            title
        ),

        product(

            name,
            price,

            inventory(

                stock_status,

                store(
                    name,
                    address,
                    latitude,
                    longitude
                )

            )

        )

        """

        )

        .execute()

    )


    data = result.data



    keyword = name.lower()



    filtered = []


    for item in data:


        anime = item.get(
            "anime"
        )


        if (

            keyword in item["name"].lower()

            or

            (
            anime
            and
            keyword in anime["title"].lower()
            )

        ):

            filtered.append(item)



    return filtered
