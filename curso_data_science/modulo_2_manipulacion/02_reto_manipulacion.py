"""Reto del Módulo 2: resumir mediciones ambientales.

Completa la función resumen_por_estacion y ejecuta este archivo. El reto
practica filtrado, columnas derivadas y agrupación con Pandas.
"""

import pandas as pd


def resumen_por_estacion(datos: pd.DataFrame) -> pd.DataFrame:
    """Devuelve métricas de temperatura agrupadas por estación.

    La función debe devolver las columnas:
    - estacion
    - mediciones
    - temperatura_promedio
    - anomalias

    Una anomalía es una temperatura menor que 10 o mayor que 24 grados Celsius.
    Las filas cuya temperatura sea faltante no cuentan como mediciones válidas.

    Args:
        datos: DataFrame con las columnas estacion y temperatura.

    Returns:
        DataFrame ordenado por estación y con una fila por estación.
    """
    # TODO: Tu código aquí
    pass


DATOS_PRUEBA = pd.DataFrame({
    "estacion": ["Norte", "Sur", "Norte", "Centro", "Sur", "Centro"],
    "temperatura": [18.5, 25.4, 19.2, 8.9, 26.1, None],
})


# Casos de prueba: deben pasar después de completar la función.
resultado = resumen_por_estacion(DATOS_PRUEBA)
assert list(resultado.columns) == [
    "estacion",
    "mediciones",
    "temperatura_promedio",
    "anomalias",
]
assert resultado["estacion"].tolist() == ["Centro", "Norte", "Sur"]
assert resultado["mediciones"].tolist() == [1, 2, 2]
assert resultado["anomalias"].tolist() == [1, 0, 2]
assert resultado["temperatura_promedio"].round(1).tolist() == [8.9, 18.9, 25.8]

print("Todos los casos de prueba pasaron.")
