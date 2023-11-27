from fastapi import APIRouter
from ..schemas.upload_schema import UploadResponseSchema

router = APIRouter()


@router.post("/upload/", response_model=UploadResponseSchema)
async def upload_file():
    pass
