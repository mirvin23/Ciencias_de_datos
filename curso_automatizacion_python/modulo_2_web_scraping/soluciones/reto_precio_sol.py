"""Solución docente para extraer producto y precio desde HTML."""

from bs4 import BeautifulSoup


def extraer_producto_y_precio(html: str) -> tuple[str, float]:
    """Extrae producto y precio desde los selectores de práctica."""
    sopa = BeautifulSoup(html, "html.parser")
    producto = sopa.select_one(".producto")
    precio = sopa.select_one(".precio")
    if producto is None or precio is None:
        raise ValueError("HTML sin producto o precio")
    valor = precio.get_text(strip=True).replace("$", "").replace(",", "")
    return producto.get_text(strip=True), float(valor)
