from fastapi import APIRouter
from database.supabase import supabase


router = APIRouter()


@router.get("/stores")
def get_stores():


    result = (
        supabase
        .table("store")
        .select("*")
        .execute()
    )


    return result.data
