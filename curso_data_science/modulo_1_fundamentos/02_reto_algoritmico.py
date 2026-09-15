"""Reto algorítmico del Módulo 1.

Completa la función es_palindromo y ejecuta este archivo para comprobar tu
solución con los casos de prueba incluidos.
"""


def es_palindromo(texto: str) -> bool:
    """Indica si texto se lee igual al derecho y al revés.

    La comparación debe ignorar espacios, signos de puntuación y diferencias
    entre mayúsculas y minúsculas. Por ejemplo, "Anita lava la tina" debe
    devolver True.

    Args:
        texto: Cadena que se desea analizar.

    Returns:
        True si el texto normalizado es un palíndromo; en caso contrario,
        False.
    """
    # TODO: Tu código aquí
    pass


# Casos de prueba: ejecútalos después de completar la función.
assert es_palindromo("reconocer") is True
assert es_palindromo("Anita lava la tina") is True
assert es_palindromo("A man, a plan, a canal: Panama!") is True
assert es_palindromo("Python") is False
assert es_palindromo("Datos y ciencia") is False
assert es_palindromo("") is True
assert es_palindromo("...") is True

print("Todos los casos de prueba pasaron.")
