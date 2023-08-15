from handler import BaseHandler


class MessageHandler(BaseHandler):
    async def receive_request(self) -> str:
        return await self.websocket.receive_text()

    async def send_response(self, response: str) -> None:
        await self.websocket.send_text(response)