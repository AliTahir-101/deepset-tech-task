from fastapi import APIRouter
from ..schemas.upload import UploadResponseSchema

router = APIRouter()


@router.post("/upload/", response_model=UploadResponseSchema)
async def upload_file():
    pass
