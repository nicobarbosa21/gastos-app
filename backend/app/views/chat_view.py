from fastapi import APIRouter
from app.controllers.chat_controller import ChatController
from app.models.message_model import MessageRequest, MessageResponse

router = APIRouter()
chat_controller = ChatController()

@router.post("/chat", response_model=MessageResponse)
async def chat(message: MessageRequest):
    return await chat_controller.handle_message(message)

@router.post("/reset/{chat_id}")
def reset_chat(chat_id: str):
    from app.services.chat_context import reset_sesion
    reset_sesion(chat_id)
    return {"status": "Sesion reiniciada"}
