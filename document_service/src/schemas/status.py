from pydantic import BaseModel

# This schema defines the structure of the response for a file status request.
# It includes the file_id and the current status which can be 'processing', 'completed', or 'error'.


class FileStatusResponseSchema(BaseModel):
    file_id: str
    status: str
