"""Solución docente simplificada del reto de reportes."""

from pathlib import Path
import re
from openpyxl import load_workbook
from docx import Document


def nombre_seguro(nombre: str) -> str:
    """Convierte un nombre en un fragmento seguro para usar como archivo."""
    return re.sub(r"[^A-Za-z0-9_-]+", "_", nombre).strip("_") or "cliente"


def generar_reportes(ruta_excel: Path, carpeta_salida: Path, modo_prueba: bool = True) -> list[Path]:
    """Genera documentos Word de reporte y devuelve sus rutas."""
    if not ruta_excel.exists():
        return []
    libro = load_workbook(ruta_excel, read_only=True, data_only=True)
    try:
        hoja = libro.active
        filas = list(hoja.iter_rows(values_only=True))
    finally:
        libro.close()
    encabezados = [str(valor).strip().lower() for valor in filas[0]]
    requeridos = {"nombre", "correo", "total"}
    if not requeridos.issubset(encabezados):
        raise ValueError("Faltan columnas requeridas")
    indices = {nombre: encabezados.index(nombre) for nombre in requeridos}
    rutas = []
    for fila in filas[1:]:
        nombre = str(fila[indices["nombre"]])
        salida = carpeta_salida / f"reporte_{nombre_seguro(nombre)}.docx"
        rutas.append(salida)
        if not modo_prueba:
            carpeta_salida.mkdir(parents=True, exist_ok=True)
            documento = Document()
            documento.add_heading(f"Reporte de {nombre}", level=1)
            documento.add_paragraph(f"Correo: {fila[indices['correo']]}")
            documento.add_paragraph(f"Total: {fila[indices['total']]}")
            documento.save(salida)
    return rutas
