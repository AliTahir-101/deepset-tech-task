from pydantic import BaseModel


class UploadResponseSchema(BaseModel):
    file_id: str
    status: str
