from dotenv import load_dotenv
import os
from agents import Agent
from agents.extensions.handoff_prompt import prompt_with_handoff_instructions
from app.prompts.prompts import (
    prompt_orquestador,
    prompt_costos,
    prompt_reporte,
    prompt_soporte_tecnico
)

load_dotenv()

# --- Agente Costos ---
agente_costos = Agent(
    name="CostosAgent",
    model="gpt-4.1",
    instructions=prompt_costos()
)

# --- Agente Reporte ---
agente_reporte = Agent(
    name="ReporteAgent",
    model="gpt-4.1",
    instructions=prompt_reporte()
)

# --- Agente Soporte Tecnico ---
agente_soporte_tecnico = Agent(
    name="SoporteTecnicoAgent",
    model="gpt-4.1",
    instructions=prompt_soporte_tecnico()
)

# --- Agente Orquestador ---
agente_orquestador = Agent(
    name="OrquestadorAgent",
    model="gpt-4.1",
    instructions=prompt_with_handoff_instructions(prompt_orquestador()),
    handoffs=[agente_costos, agente_reporte, agente_soporte_tecnico],
)