from fastapi import APIRouter

from app.schemas.sche_base import DataResponse
from app.services.scraper import scraper
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
router = APIRouter()

@router.get("")
async def getScrapercheck(url: str):
    try:
        html=scraper(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)