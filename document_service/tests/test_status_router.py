from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from src.main import app
from src.services.status import StatusService

import pytest


class TestStatusEndpoint:
    @pytest.fixture(autouse=True)
    def setup_class(self):
        self.client = TestClient(app)
        # Mock the status service dependency
        self.mock_status_service = MagicMock()
        app.dependency_overrides[StatusService] = lambda: self.mock_status_service

    def test_get_file_status(self):
        test_file_id = "unique_file_id"
        expected_status = "processing"
        # Configure the mock to return a specific status
        self.mock_status_service.get_status.return_value = expected_status

        response = self.client.get(f"/status/{test_file_id}")

        # Assert that the status service was called with the correct file ID
        self.mock_status_service.get_status.assert_called_with(test_file_id)

        assert response.status_code == 200
        assert response.json() == {
            "file_id": test_file_id, "status": expected_status}

    # Teardown any dependency overrides after the tests
    def teardown_method(self):
        app.dependency_overrides = {}

# Additional tests here...
