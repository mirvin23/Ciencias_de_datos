"""Solución docente segura: modo prueba y programación cancelable."""

import schedule


def enviar_mensaje(mensaje: str, modo_prueba: bool = True) -> str:
    """Devuelve una acción simulada o ejecuta una integración autorizada."""
    mensaje = mensaje.strip()
    if not mensaje:
        raise ValueError("El mensaje no puede estar vacío")
    if modo_prueba:
        return f"SIMULACIÓN: enviar mensaje de {len(mensaje)} caracteres"
    raise RuntimeError("Conecta aquí una aplicación autorizada y validada")


def configurar_tarea(hora: str, mensaje: str):
    """Programa una tarea diaria sin iniciar un bucle permanente."""
    return schedule.every().day.at(hora).do(enviar_mensaje, mensaje, True)
