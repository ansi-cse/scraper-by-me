from fastapi import APIRouter

from app.schemas.sche_base import ResponseSchemaBase

router = APIRouter()


@router.get("", response_model=ResponseSchemaBase)
async def getHealthcheck():
    return {"message": "Health check success"}