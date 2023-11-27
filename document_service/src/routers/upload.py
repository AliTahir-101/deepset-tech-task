import logging

from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from ..services.storage import StorageService
from ..services.message_queue import MessageQueueService
from ..schemas.upload import UploadResponseSchema

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/api/v1/files/", response_model=UploadResponseSchema)
async def upload_file(
    background_tasks: BackgroundTasks,
    storage_service: StorageService,
    message_queue_service: MessageQueueService,
    file: UploadFile = File(...),
):
    try:
        # Saves the file to Azure Blob raw storage and get the reference ID
        file_reference = await storage_service.save_file_to_blob(file)
        # Sends a message to Kafka for the file to be processed
        background_tasks.add_task(
            message_queue_service.send_message, file_reference)
        return {"file_id": file_reference, "status": "File uploaded and processing queued"}
    except Exception as e:
        logger.exception(f"Failed to upload file: {e}")
        raise HTTPException(status_code=500, detail=str(e))
