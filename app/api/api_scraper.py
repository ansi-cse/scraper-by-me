from fastapi import APIRouter
import os
from app.services.scraper import  base, getImage, nhaTot, tests, bdscom, bdscomInvestor
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
from fastapi.responses import FileResponse
import traceback
from loguru import logger
from app.helpers.chromeDriverPool import ScrapeThread
router = APIRouter()
logger.add("app.log", rotation="500 MB")

@router.get("")
async def getScraperFor(url: str):
    try:
        logger.info("Creating new Chrome driver instance")
        html=base(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        traceback.print_exc()
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/getImage")
async def getScraperFor(url: str):
    try:
        image=getImage(url)
        return FileResponse(image, media_type="image/jpeg", filename=image)
    except Exception:
        traceback.print_exc()
        return HTMLResponse(content="Fail to load page", status_code=400)
    finally:
        if os.path.exists(image):
            os.remove(image)

@router.get("/nhatot")
async def getScraperForNhaTot(url: str):
    try:
        html=nhaTot(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/bdscom")
async def getScraperForBdsCom(url: str):
    try:
        logger.info(url)
        html=bdscom(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)
@router.get("/bdscom/investor")
async def getScraperForBdsCom(url: str):
    try:
        logger.info(url)
        html=bdscomInvestor(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)


@router.get("/test")
async def test(url: str):
    t = ScrapeThread(url)
    t.start()
    t.join()
    page_source = t.get_page_source()
    return {"results": page_source}
    