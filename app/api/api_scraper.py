from fastapi import APIRouter
import os
from app.services.scraper import base, getImage, nhaTot, tests, bdscom, bdscomInvestor, bdscomPersonalBroker, bdscomEnterpriseBroker
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
from fastapi.responses import FileResponse
import traceback
from loguru import logger
from app.helpers.scraperThreading import ScrapeThread
from pixelbin import PixelbinClient, PixelbinConfig
from app.helpers.image import blur_center
router = APIRouter()


@router.get("")
async def getScraperFor(url: str):
    try:
        html = await base(url)
        result = str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except:
        traceback.print_exc()
        return HTMLResponse(content="Fail to load page", status_code=400)


@router.get("/getImage")
async def getScraperFor(url: str):
    image = ""
    try:
        image = await getImage(url)
        return FileResponse(image, media_type="image/jpeg", filename=image)
    except Exception:
        traceback.print_exc()
        return HTMLResponse(content="Fail to load page", status_code=400)
    # finally:
    #     if os.path.exists(image):
    #         os.remove(image)


@router.get("/nhatot")
async def getScraperForNhaTot(url: str):
    try:
        html = await nhaTot(url)
        result = str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except:
        return HTMLResponse(content="Fail to load page", status_code=400)


@router.get("/bdscom")
async def getScraperForBdsCom(url: str):
    try:
        # html= bdscom(url)
        html = await bdscom(url)
        result = str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except Exception as e:
        import traceback
        traceback.print_exc()  # Print the stack trace
        return HTMLResponse(content="Fail to load page", status_code=400)


@router.get("/bdscom/investor")
async def getScraperForBdsCom(url: str):
    try:
        logger.info(url)
        html = bdscomInvestor(url)
        result = str(BeautifulSoup(html))
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
        html = bdscomEnterpriseBroker(url)
        result = str(BeautifulSoup(html))
        return HTMLResponse(content=result, status_code=200)
    except:
        return HTMLResponse(content="Fail to load page", status_code=400)


@router.get("/bdscom/personalBroker")
async def getPersonalBrokerForBdsCom(url: str):
    try:
        logger.info(url)
        html = bdscomPersonalBroker(url)
        result = str(BeautifulSoup(html))
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
        urlFromPixelbin = await pixelbin.assets.urlUploadAsync(url=url)
        return urlFromPixelbin
    except Exception as e:
        return {"error": str(e)}

import cv2
from urllib.parse import urlparse
@router.get("/images/blur")
async def list_assets(url: str):
    image = ""
    try:
        image = await getImage(url)
        blurred_image=blur_center(image_path=image, width=130, height=45, sigmaX=7)
        parseTofileName=urlparse(url).path.split("/")
        fileName=parseTofileName[len(parseTofileName)-1]
        blurred_image_path = fileName
        cv2.imwrite(blurred_image_path, blurred_image)
        # Trả về tệp tạm thời làm mờ dưới dạng phản hồi từ server
        return FileResponse(blurred_image_path, media_type="image/jpeg")
    except Exception:
        traceback.print_exc()
        return HTMLResponse(content="Fail to load page", status_code=400)


@router.get("/test")
async def test(url: str):
    for x in range(0, 10):
        t = ScrapeThread(url, True, True)
        t.start()
        t.join()
        page_source = t.get_page_source()
    return {"results": "ok"}


