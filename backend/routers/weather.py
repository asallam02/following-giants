from fastapi import APIRouter
# from services.weather_service import get_weather_summary

router = APIRouter(prefix="/weather", tags=["weather"])

@router.get("/")
def weather_summary():
    pass
    # return get_weather_summary()
