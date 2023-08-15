from fastapi import WebSocket
from typing import Any

class BaseHandler:
    def __init__(self, websocket: WebSocket):
        self.websocket = websocket

    async def receive_request(self) -> Any:
        """Receive a request from the client."""
        raise NotImplementedError("Subclasses must implement this method.")

    async def send_response(self, response: Any) -> None:
        """Send a response to the client."""
        raise NotImplementedError("Subclasses must implement this method.")

    async def handle(self) -> None:
        """Main method to handle the request and send the response."""
        request = await self.receive_request()
        
        # Here you can process the request, e.g., log it, validate it, etc.
        
        response = f"Request received: {request}"  # Placeholder response
        await self.send_response(response)