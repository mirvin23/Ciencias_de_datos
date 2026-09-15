"""Flujo de referencia para el proyecto integrador.

Material exclusivo del docente. Sirve para comprobar que el dataset y el flujo
completo producen resultados coherentes; no es una respuesta única del alumno.
"""

from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


DATASET = Path(__file__).parents[2] / "datasets" / "mediciones_integrador.csv"


def cargar_datos() -> pd.DataFrame:
    """Carga el dataset central y convierte fecha a tipo datetime."""
    return pd.read_csv(DATASET, parse_dates=["fecha"])


def crear_resumen(datos: pd.DataFrame) -> pd.DataFrame:
    """Resume mediciones y proporción de alertas por estación."""
    resumen = (
        datos.groupby("estacion", as_index=False)
        .agg(
            mediciones=("estado", "size"),
            temperatura_promedio=("temperatura", "mean"),
            humedad_promedio=("humedad", "mean"),
            alertas=("estado", lambda valores: (valores == "revisar").sum()),
        )
    )
    resumen["proporcion_alertas"] = resumen["alertas"] / resumen["mediciones"]
    return resumen.sort_values("proporcion_alertas", ascending=False)


def entrenar_y_evaluar(datos: pd.DataFrame) -> dict:
    """Entrena un árbol y devuelve métricas para el análisis docente."""
    columnas = ["temperatura", "humedad", "precipitacion_mm"]
    X = datos[columnas]
    y = datos["estado"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, predicciones),
        "report": classification_report(y_test, predicciones, zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, predicciones, labels=["normal", "revisar"]),
    }


if __name__ == "__main__":
    datos = cargar_datos()
    print(crear_resumen(datos))
    print(entrenar_y_evaluar(datos))
