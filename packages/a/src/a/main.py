"""Main application for Sample Package A."""

import asyncio
import json
from typing import Dict, Any

import click
import httpx
from pydantic import BaseModel, Field


class ApiResponse(BaseModel):
    """Model for API response data......."""
    
    status: str
    message: str
    data: Dict[str, Any] = Field(default_factory=dict)
    timestamp: str


class SampleService:
    """Sample service demonstrating basic functionality."""
    
    def __init__(self, base_url: str = "https://httpbin.org"):
        self.base_url = base_url
    
    async def get_ip_info(self) -> Dict[str, Any]:
        """Fetch IP information from external service."""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/ip")
            response.raise_for_status()
            return response.json()
    
    async def post_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Post data to external service."""
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/post", json=data)
            response.raise_for_status()
            return response.json()
    
    def process_data(self, input_data: Dict[str, Any]) -> ApiResponse:
        """Process input data and return structured response."""
        processed_data = {
            "input_keys": list(input_data.keys()),
            "input_count": len(input_data),
            "processed": True
        }
        
        return ApiResponse(
            status="success",
            message="Data processed successfully",
            data=processed_data,
            timestamp=str(asyncio.get_event_loop().time())
        )


@click.group()
@click.version_option(version="0.0.0", prog_name="sample-a")
def cli() -> None:
    """Sample Package A CLI - Demonstrating release-please automation."""
    pass


@cli.command()
@click.option("--format", "-f", type=click.Choice(["json", "pretty"]), default="pretty", help="Output format")
def info(format: str) -> None:
    """Get IP information."""
    service = SampleService()
    
    async def get_info():
        try:
            data = await service.get_ip_info()
            if format == "json":
                click.echo(json.dumps(data, indent=2))
            else:
                click.echo(f"Your IP: {data.get('origin', 'Unknown')}")
        except Exception as e:
            click.echo(f"Error: {e}", err=True)
    
    asyncio.run(get_info())


@cli.command()
@click.option("--key", "-k", multiple=True, help="Key-value pairs (key=value)")
@click.option("--format", "-f", type=click.Choice(["json", "pretty"]), default="pretty", help="Output format")
def process(key: tuple, format: str) -> None:
    """Process input data."""
    service = SampleService()
    
    # Parse key-value pairs
    input_data = {}
    for kv in key:
        if "=" in kv:
            k, v = kv.split("=", 1)
            input_data[k] = v
    
    if not input_data:
        input_data = {"example": "data", "sample": "value"}
    
    result = service.process_data(input_data)
    
    if format == "json":
        click.echo(result.model_dump_json(indent=2))
    else:
        click.echo(f"Status: {result.status}")
        click.echo(f"Message: {result.message}")
        click.echo(f"Processed {result.data.get('input_count', 0)} items")


@cli.command()
@click.option("--data", "-d", help="JSON data to send")
def send(data: str) -> None:
    """Send data to external service."""
    service = SampleService()
    
    async def send_data():
        try:
            payload = json.loads(data) if data else {"sample": "payload", "from": "sample-a"}
            result = await service.post_data(payload)
            
            click.echo("Response received:")
            click.echo(json.dumps(result.get("json", {}), indent=2))
        except json.JSONDecodeError:
            click.echo("Error: Invalid JSON data", err=True)
        except Exception as e:
            click.echo(f"Error: {e}", err=True)
    
    asyncio.run(send_data())


if __name__ == "__main__":
    cli()