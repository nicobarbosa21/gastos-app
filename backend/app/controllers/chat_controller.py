from app.models.message_model import MessageRequest, MessageResponse
from app.services.agent_service import AgentService

class ChatController:
    def __init__(self):
        self.agent_service = AgentService()

    async def handle_message(self, request: MessageRequest) -> MessageResponse:
        response_text = await self.agent_service.process_message(
            chat_id=request.chat_id,
            user_message=request.message
        )
        return MessageResponse(response=response_text)