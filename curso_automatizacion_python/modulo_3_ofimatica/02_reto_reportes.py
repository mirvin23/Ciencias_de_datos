"""Reto del estudiante: generar reportes por cliente."""

from pathlib import Path


def generar_reportes(ruta_excel: Path, carpeta_salida: Path, modo_prueba: bool = True) -> list[Path]:
    """Genera un reporte por fila de cliente y devuelve las rutas planeadas.

    Columnas mínimas: nombre, correo, total.
    En modo_prueba no crea archivos.
    """
    # TODO: carga el libro con openpyxl.
    # TODO: valida encabezados y recorre filas.
    # TODO: construye un nombre de salida seguro.
    # TODO: genera el documento solo si modo_prueba es False.
    pass


assert generar_reportes(Path("clientes.xlsx"), Path(
    "reportes"), modo_prueba=True) == []
print("Modo de prueba listo.")
