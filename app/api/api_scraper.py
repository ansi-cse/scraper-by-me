from fastapi import APIRouter

from app.services.scraper import  base, getImage, nhaTot, tests, bdscom
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
from fastapi.responses import FileResponse
import os
import cv2
import numpy as np
from PIL import Image, ImageEnhance
import cv2
import numpy as np
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
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/getImage")
async def getScraperFor(url: str):
    try:
        image=getImage(url)
        img = cv2.imread(image)
        mask = cv2.imread('mask.png', cv2.IMREAD_GRAYSCALE)
        (h,w,_)= img.shape
        _, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
        # mask=cv2.resize(mask,(w, h))
        cv2.imwrite('mask1.png', mask)
        dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        cv2.imwrite('dst.jpg', dst)
        return FileResponse(dst, media_type="image/jpeg", filename=image)
    except Exception:
        traceback.print_exc()
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/nhatot")
async def getScraperForNhaTot(url: str):
    try:
        html=nhaTot(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/bdscom")
async def getScraperForNhaTot(url: str):
    try:
        logger.info("Creating new Chrome driver instance")
        html=bdscom(url)
        logger.info("Chrome driver instance created successfully")
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
    