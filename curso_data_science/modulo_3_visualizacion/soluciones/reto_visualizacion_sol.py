"""Solución docente del reto de visualización del Módulo 3."""

import pandas as pd


def resumen_visual(datos: pd.DataFrame) -> pd.DataFrame:
    """Calcula promedio y desviación estándar de temperatura por estación."""
    return (
        datos.groupby("estacion", as_index=False)
        .agg(
            temperatura_promedio=("temperatura", "mean"),
            temperatura_desviacion=("temperatura", "std"),
        )
        .sort_values("temperatura_promedio", ascending=False)
        .reset_index(drop=True)
    )


def correlacion_temperatura_humedad(datos: pd.DataFrame) -> float:
    """Calcula la correlación lineal entre temperatura y humedad."""
    return float(datos["temperatura"].corr(datos["humedad"]))


if __name__ == "__main__":
    datos_prueba = pd.DataFrame({
        "estacion": ["Norte", "Norte", "Sur", "Sur", "Centro", "Centro"],
        "temperatura": [18.5, 19.5, 25.0, 27.0, 10.0, 12.0],
        "humedad": [55.0, 57.0, 61.0, 59.0, 72.0, 70.0],
    })
    print(resumen_visual(datos_prueba))
    print("Correlación:", correlacion_temperatura_humedad(datos_prueba))
