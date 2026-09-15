"""Solución docente del reto de manipulación del Módulo 2."""

import pandas as pd


def resumen_por_estacion(datos: pd.DataFrame) -> pd.DataFrame:
    """Calcula métricas de temperatura válidas y anomalías por estación."""
    datos_validos = datos.dropna(subset=["temperatura"]).copy()
    datos_validos["anomalia"] = (
        (datos_validos["temperatura"] < 10)
        | (datos_validos["temperatura"] > 24)
    )

    return (
        datos_validos.groupby("estacion", as_index=False)
        .agg(
            mediciones=("temperatura", "count"),
            temperatura_promedio=("temperatura", "mean"),
            anomalias=("anomalia", "sum"),
        )
        .sort_values("estacion")
        .reset_index(drop=True)
    )


if __name__ == "__main__":
    datos_prueba = pd.DataFrame({
        "estacion": ["Norte", "Sur", "Norte", "Centro", "Sur", "Centro"],
        "temperatura": [18.5, 25.4, 19.2, 8.9, 26.1, None],
    })
    print(resumen_por_estacion(datos_prueba))
