"""Solución docente del reto de Machine Learning del Módulo 4."""

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def entrenar_clasificador(datos: pd.DataFrame):
    """Entrena un árbol de decisión con dos características ambientales."""
    X = datos[["temperatura", "humedad"]]
    y = datos["estado"]
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )
    modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
    modelo.fit(X_entrenamiento, y_entrenamiento)
    return modelo, X_prueba, y_prueba


def evaluar_modelo(modelo, X_prueba: pd.DataFrame, y_prueba: pd.Series) -> float:
    """Calcula la exactitud sobre datos reservados."""
    predicciones = modelo.predict(X_prueba)
    return float(accuracy_score(y_prueba, predicciones))


if __name__ == "__main__":
    datos_prueba = pd.DataFrame({
        "temperatura": [18.5, 19.2, 25.4, 26.1, 8.9, 21.0, 22.4, 27.0, 17.5, 24.8, 10.0, 20.5],
        "humedad": [55, 58, 61, 59, 72, 64, 60, 57, 56, 62, 70, 65],
        "estado": ["normal", "normal", "revisar", "revisar", "revisar", "normal", "normal", "revisar", "normal", "revisar", "revisar", "normal"],
    })
    modelo, X_prueba, y_prueba = entrenar_clasificador(datos_prueba)
    print("Exactitud:", evaluar_modelo(modelo, X_prueba, y_prueba))
