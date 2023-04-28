from fastapi import APIRouter
import os
from app.services.scraper import  base, getImage, nhaTot, tests, bdscom, bdscomInvestor, removeWaterMask,remove, bdscomPersonalBroker, bdscomEnterpriseBroker
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
from fastapi.responses import FileResponse
import traceback
from loguru import logger
from app.helpers.scraperThreading import ScrapeThread
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig
from pixelbin.utils.url import obj_to_url,url_to_obj
router = APIRouter()

@router.get("")
async def getScraperFor(url: str):
    try:
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
        # html= bdscom(url)
        html = await bdscom(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except Exception as e:
        print(e)  # Print the error message
        import traceback
        traceback.print_exc()  # Print the stack trace
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/bdscom/investor")
async def getScraperForBdsCom(url: str):
    try:
        logger.info(url)
        html=bdscomInvestor(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except Exception as e:
        print(e)  # Print the error message
        import traceback
        traceback.print_exc()  # Print the stack trace
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/bdscom/enterpriseBroker")
async def getEnterpriseBrokerForBdsCom(url: str):
    try:
        logger.info(url)
        html=bdscomEnterpriseBroker(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

@router.get("/bdscom/personalBroker")
async def getPersonalBrokerForBdsCom(url: str):
    try:
        logger.info(url)
        html=bdscomPersonalBroker(url)
        result=str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except: 
        return HTMLResponse(content="Fail to load page", status_code=400)

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "20a231bc-cde1-4b39-881a-0a77153d9ec9",
})
pixelbin = PixelbinClient(config=config)

@router.get("/images/removewatermask")
async def list_assets(url: str):
    try:
        urlFromPixelbin =await pixelbin.assets.urlUploadAsync(url=url)
        return urlFromPixelbin
    except Exception as e:
        return {"error": str(e)}

@router.get("/test")
async def test(url: str):
    for x in range(0,10):
        t = ScrapeThread(url, True, True)
        t.start()
        t.join()
        page_source = t.get_page_source()
    return {"results": "ok"}