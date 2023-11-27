import pytest

from unittest.mock import patch
from fastapi.testclient import TestClient
from src.main import app

# This class encapsulates all the test cases for the upload endpoint.


class TestUploadEndpoint:
    # Pytest fixture for setting up the test environment before each test.
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = TestClient(app)

    # Mock the storage and message queue services for the test case of a successful file upload.
    @patch('src.services.storage.StorageService')
    @patch('src.services.message_queue.MessageQueueService')
    def test_upload_file_success(self, mock_storage_service, mock_message_queue_service):
        # Configure the mock of the StorageService to return a mock file ID.
        mock_storage_service.save_file_to_blob.return_value = "mock_file_id"

        # Simulate the file upload by posting to the /api/v1/files/ endpoint with a dummy file.
        response = self.client.post(
            "/api/v1/files/",
            files={"file": ("filename.txt", "file content")}
        )

        # Assert that the response status code is 200 OK.
        assert response.status_code == 200
        # Assert that the response JSON includes the mock file ID and the expected status message.
        assert response.json() == {
            "file_id": "mock_file_id", "status": "File uploaded and processing queued"}

    # A separate test case to handle the scenario where an upload fails due to invalid input.
    def test_upload_file_failure(self):
        # Here we simulate a file upload without providing a file, which should fail.
        response = self.client.post("/api/v1/files/")

        # Assert that the response status code is 422 Unprocessable Entity.
        assert response.status_code == 422

    # Can add more test cases as needed to cover different scenarios and edge cases.
