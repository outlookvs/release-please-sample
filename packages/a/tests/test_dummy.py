"""Tests for Sample Package A."""

import pytest
import asyncio
from unittest.mock import AsyncMock, patch

from a.main import SampleService, ApiResponse


class TestSampleService:
    """Test cases for SampleService."""
    
    def test_process_data(self):
        """Test data processing functionality."""
        service = SampleService()
        input_data = {"key1": "value1", "key2": "value2"}
        
        result = service.process_data(input_data)
        
        assert isinstance(result, ApiResponse)
        assert result.status == "success"
        assert result.message == "Data processed successfully"
        assert result.data["input_count"] == 2
        assert result.data["input_keys"] == ["key1", "key2"]
        assert result.data["processed"] is True
    
    def test_process_empty_data(self):
        """Test processing empty data."""
        service = SampleService()
        input_data = {}
        
        result = service.process_data(input_data)
        
        assert result.status == "success"
        assert result.data["input_count"] == 0
        assert result.data["input_keys"] == []
    
    @pytest.mark.asyncio
    async def test_get_ip_info(self):
        """Test IP info retrieval."""
        service = SampleService()
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.json.return_value = {"origin": "127.0.0.1"}
            mock_response.raise_for_status.return_value = None
            
            mock_client.return_value.__aenter__.return_value.get.return_value = mock_response
            
            result = await service.get_ip_info()
            
            assert result == {"origin": "127.0.0.1"}
    
    @pytest.mark.asyncio
    async def test_post_data(self):
        """Test data posting."""
        service = SampleService()
        test_data = {"test": "data"}
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_response = AsyncMock()
            mock_response.json.return_value = {"json": test_data, "status": "ok"}
            mock_response.raise_for_status.return_value = None
            
            mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
            
            result = await service.post_data(test_data)
            
            assert result == {"json": test_data, "status": "ok"}


class TestApiResponse:
    """Test cases for ApiResponse model."""
    
    def test_api_response_creation(self):
        """Test ApiResponse model creation."""
        response = ApiResponse(
            status="success",
            message="Test message",
            timestamp="123456789"
        )
        
        assert response.status == "success"
        assert response.message == "Test message"
        assert response.data == {}
        assert response.timestamp == "123456789"
    
    def test_api_response_with_data(self):
        """Test ApiResponse with custom data."""
        test_data = {"key": "value", "count": 42}
        response = ApiResponse(
            status="success",
            message="Test message",
            data=test_data,
            timestamp="123456789"
        )
        
        assert response.data == test_data