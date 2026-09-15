"""Reto del estudiante: extraer un precio de HTML permitido."""

from bs4 import BeautifulSoup


def extraer_producto_y_precio(html: str) -> tuple[str, float]:
    """Extrae texto de `.producto` y precio numérico desde HTML."""
    # TODO: analiza html con BeautifulSoup.
    # TODO: obtén los selectores `.producto` y `.precio`.
    # TODO: limpia el símbolo monetario y convierte a float.
    pass


HTML_PRUEBA = '<article><h1 class="producto">Cuaderno</h1><span class="precio">$19.90</span></article>'
nombre, precio = extraer_producto_y_precio(HTML_PRUEBA)
assert nombre == "Cuaderno"
assert precio == 19.90
print(f"{nombre}: {precio:.2f}")
