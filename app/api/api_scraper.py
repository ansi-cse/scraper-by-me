from fastapi import APIRouter

from app.services.scraper import  base, getImage, nhaTot
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("")
async def getScraperFor(url: str):
    try:
        html=base(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/getImage")
async def getScraperFor(url: str):
    try:
        image=getImage(url)
        return FileResponse(image, media_type="image/jpeg", filename="vector_image_for_you.jpg")
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/nhatot")
async def getScraperForNhaTot(url: str):
    try:
        html=nhaTot(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)