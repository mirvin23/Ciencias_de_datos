"""Reto del estudiante: bot visible con tarea programada."""

import schedule


def enviar_mensaje(mensaje: str, modo_prueba: bool = True) -> str:
    """Prepara un mensaje y, si se autoriza, ejecuta acciones visibles.

    La primera versión debe funcionar en modo prueba sin mover el ratón.
    """
    # TODO: valida que mensaje no esté vacío.
    # TODO: en modo prueba, devuelve una descripción de la acción.
    # TODO: deja las acciones pyautogui para una aplicación autorizada.
    pass


def configurar_tarea(hora: str, mensaje: str):
    """Programa el envío diario y devuelve el objeto de tarea."""
    # TODO: usa schedule.every().day.at(hora).do(...).
    pass


resultado = enviar_mensaje("Mensaje de prueba", modo_prueba=True)
assert isinstance(resultado, str)
print(resultado)
