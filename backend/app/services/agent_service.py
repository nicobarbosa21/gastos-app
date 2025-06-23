from agents import Runner
from app.services.agent_loader import agente_orquestador
from app.services.chat_context import get_sesion

class AgentService:
    async def process_message(self, chat_id: str, user_message: str) -> str:
        sesion = get_sesion(chat_id)
        sesion.nuevo_mensaje(user_message)

        historial = sesion.obtener_historial()

        prompt = "\n".join(historial) + f"\n\nUsuario: {user_message}\nAsistente:"

        resultado = await Runner.run(agente_orquestador, prompt)

        return resultado.final_output