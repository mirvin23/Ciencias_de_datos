# Módulo 2: Extracción de Datos y Web Scraping

## Reto

Construir un extractor que lea el nombre y precio de un producto desde HTML permitido y avise si baja de un umbral.

## Flujo

```text
URL permitida -> solicitud -> respuesta -> HTML -> selector -> precio -> decisión
```

## Librerías

- `requests`: solicitudes HTTP con timeout.
- `BeautifulSoup`: análisis del HTML.
- `re` o conversión controlada: limpieza del precio.

## Uso responsable

- Revisa `robots.txt`, términos de uso y permisos.
- Usa `timeout` y pausas entre solicitudes.
- No evadas controles ni recopiles datos personales.
- Practica primero con HTML local o una API pública.
- Identifica la fuente y la fecha de extracción.

## Ejemplo

```python
import requests
from bs4 import BeautifulSoup

respuesta = requests.get(url, timeout=10)
respuesta.raise_for_status()
sopa = BeautifulSoup(respuesta.text, "html.parser")
precio = sopa.select_one(".precio")
```

## Entrega

El script debe recibir una URL o HTML de práctica, extraer producto y precio, convertir el precio a número y mostrar una alerta si está bajo el umbral.

## Evaluación

- solicitud responsable: 25%; parsing: 25%; conversión: 25%; errores y documentación: 25%.
