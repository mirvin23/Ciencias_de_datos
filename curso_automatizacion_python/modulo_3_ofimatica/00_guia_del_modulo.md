# Módulo 3: Automatización de Ofimática

## Reto

Leer clientes desde Excel, generar un documento personalizado y producir un PDF por cliente.

## Flujo

```text
Excel -> validar filas -> plantilla -> documento -> PDF -> carpeta de reportes
```

## Librerías

- `openpyxl`: leer hojas de cálculo.
- `python-docx`: generar Word.
- `PyPDF2`: leer, combinar o inspeccionar PDFs.
- `reportlab`: crear PDFs directamente cuando sea necesario.

## Seguridad y calidad

- Valida columnas requeridas.
- No expongas datos personales en logs.
- Usa una carpeta de salida separada.
- No sobrescribas reportes sin confirmación.
- Comprueba que cada cliente produjo un archivo.

## Ejemplo de lectura

```python
from openpyxl import load_workbook

libro = load_workbook("clientes.xlsx", read_only=True, data_only=True)
hoja = libro.active
for fila in hoja.iter_rows(min_row=2, values_only=True):
    print(fila)
```

## Entrega

Genera un reporte por cliente con nombre seguro, valida el total de filas y registra errores sin detener todo el lote.

## Evaluación

- lectura y validación: 25%; personalización: 25%; salida PDF: 25%; trazabilidad y privacidad: 25%.
