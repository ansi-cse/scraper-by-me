from fastapi import APIRouter

from app.api import api_healthcheck, api_scraper

router = APIRouter()

router.include_router(api_healthcheck.router, tags=["health-check"], prefix="/healthcheck")
router.include_router(api_scraper.router, tags=["scraper"], prefix="/scraper")