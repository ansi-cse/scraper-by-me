from fastapi import APIRouter

from app.schemas.sche_base import DataResponse
from app.services.scraper import NhaTot, Base, GetImage
from fastapi.responses import HTMLResponse
from fastapi.responses import ORJSONResponse
from bs4 import BeautifulSoup
router = APIRouter()

@router.get("")
async def getScraperFor(url: str):
    try:
        html=Base(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/getImage")
async def getScraperFor(url: str):
    try:
        image=GetImage(url)
        return HTMLResponse(content=image, media_type="image/png", status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/nhatot")
async def getScraperForNhaTot(url: str):
    try:
        html=NhaTot(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)