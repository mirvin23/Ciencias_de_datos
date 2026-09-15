"""Reto del Módulo 3: análisis visual de mediciones ambientales.

Completa las funciones para calcular un resumen y la correlación. Los gráficos
se desarrollan en el notebook para que puedas observarlos y comentarlos.
"""

import pandas as pd


def resumen_visual(datos: pd.DataFrame) -> pd.DataFrame:
    """Devuelve el promedio y la desviación estándar por estación.

    Args:
        datos: DataFrame con las columnas estacion y temperatura.

    Returns:
        DataFrame con estacion, temperatura_promedio y temperatura_desviacion,
        ordenado de mayor a menor temperatura promedio.
    """
    # TODO: Tu código aquí
    pass


def correlacion_temperatura_humedad(datos: pd.DataFrame) -> float:
    """Calcula la correlación lineal entre temperatura y humedad."""
    # TODO: Tu código aquí
    pass


DATOS_PRUEBA = pd.DataFrame({
    "estacion": ["Norte", "Norte", "Sur", "Sur", "Centro", "Centro"],
    "temperatura": [18.5, 19.5, 25.0, 27.0, 10.0, 12.0],
    "humedad": [55.0, 57.0, 61.0, 59.0, 72.0, 70.0],
})


# Casos de prueba: deben pasar cuando completes las funciones.
resumen = resumen_visual(DATOS_PRUEBA)
assert resumen["estacion"].tolist() == ["Sur", "Norte", "Centro"]
assert resumen["temperatura_promedio"].round(1).tolist() == [26.0, 19.0, 11.0]
assert list(resumen.columns) == [
    "estacion",
    "temperatura_promedio",
    "temperatura_desviacion",
]

correlacion = correlacion_temperatura_humedad(DATOS_PRUEBA)
assert -1.0 <= correlacion <= 1.0

print("Todos los casos de prueba pasaron.")
