import logging

from fastapi import APIRouter, HTTPException, Path, Depends
from ..services.status import StatusService
from ..schemas.status import FileStatusResponseSchema

logger = logging.getLogger(__name__)

router = APIRouter()

# Endpoint to check the processing status of an uploaded file.
# GET /files/{file_id}/status
# The response model is defined in FileStatusResponseSchema which ensures consistent API responses.
# StatusService is injected as a dependency for retrieving the file status.


@router.get("/api/v1/files/{file_id}/status", response_model=FileStatusResponseSchema)
async def check_file_status(
    # Path parameter to capture the file ID from the URL.
    file_id: str = Path(...),
    # Dependency injection of the StatusService.
    status_service: StatusService = Depends(StatusService)
):
    try:
        # Retrieves the current status of the file based on the file_id provided.
        status = await status_service.get_status(file_id)
        return FileStatusResponseSchema(file_id=file_id, status=status)
    except Exception as e:
        logger.exception(f"Error retrieving file status: {e}")
        # Can Setup Different HTTP status codes based on the type of error.
        raise HTTPException(status_code=500, detail=str(e))
