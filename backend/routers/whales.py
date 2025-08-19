from fastapi import APIRouter, Query
from services.whale_service import load_blue_whale_data

router = APIRouter(prefix="/whales", tags=["Whales"])

@router.get("/")
def whales():
    return "whales page"

@router.get("/blue")
def get_blue_whales(limit: int = Query(100, description="Max number of records to return")):
    """
    Return blue whale occurrence records (latitude, longitude, date, etc.)
    """
    return load_blue_whale_data(limit)
