from datetime import datetime
from app.models.mensaje import mensaje

class Sesion:
    def __init__(self, chat_id: str):
        self.chat_id = chat_id
        self.fechaHoraInicio = datetime.now()
        self.fechaHoraFin = ""
        self.estado = ""
        self.historial = []

    def nuevo_mensaje(self, contenido):
        msg = mensaje(contenido)
        self.historial.append(msg)

    def obtener_historial(self):
        return [m.contenido for m in self.historial]