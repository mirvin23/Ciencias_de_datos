"""Reto del Módulo 4: entrenar y evaluar un clasificador.

Completa las funciones y ejecuta este archivo. El objetivo es practicar la
separación entre datos de entrenamiento y prueba y la evaluación de un modelo.
"""

import pandas as pd


def entrenar_clasificador(datos: pd.DataFrame):
    """Entrena un árbol de decisión y devuelve modelo, X_prueba e y_prueba.

    Usa como características temperatura y humedad. Usa estado como objetivo.
    La separación debe usar test_size=0.25, random_state=42 y stratify.

    Args:
        datos: DataFrame con temperatura, humedad y estado.

    Returns:
        Tupla con el modelo entrenado, X_prueba e y_prueba.
    """
    # TODO: Tu código aquí
    pass


def evaluar_modelo(modelo, X_prueba: pd.DataFrame, y_prueba: pd.Series) -> float:
    """Devuelve la exactitud del modelo sobre los datos de prueba."""
    # TODO: Tu código aquí
    pass


DATOS_PRUEBA = pd.DataFrame({
    "temperatura": [18.5, 19.2, 25.4, 26.1, 8.9, 21.0, 22.4, 27.0, 17.5, 24.8, 10.0, 20.5],
    "humedad": [55, 58, 61, 59, 72, 64, 60, 57, 56, 62, 70, 65],
    "estado": ["normal", "normal", "revisar", "revisar", "revisar", "normal", "normal", "revisar", "normal", "revisar", "revisar", "normal"],
})


# Casos de prueba: deben pasar al completar las funciones.
modelo, X_prueba, y_prueba = entrenar_clasificador(DATOS_PRUEBA)
assert list(X_prueba.columns) == ["temperatura", "humedad"]
assert len(X_prueba) == 3
assert len(y_prueba) == 3

exactitud = evaluar_modelo(modelo, X_prueba, y_prueba)
assert 0.0 <= exactitud <= 1.0

print("Todos los casos de prueba pasaron.")
