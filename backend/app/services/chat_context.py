from app.models.sesion import Sesion

# Diccionario global para gestionar sesiones activas
sesiones = {}

def get_sesion(chat_id: str) -> Sesion:
    if chat_id not in sesiones:
        sesiones[chat_id] = Sesion(chat_id)
    return sesiones[chat_id]

def reset_sesion(chat_id: str):
    if chat_id in sesiones:
        del sesiones[chat_id]
