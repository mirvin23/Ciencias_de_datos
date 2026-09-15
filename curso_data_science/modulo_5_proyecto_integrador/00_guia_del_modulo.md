# Módulo 5: Proyecto Integrador de Ciencia de Datos

## Propósito

Este módulo integra el flujo completo del curso: Python, estructuras de datos, Pandas, visualización y Machine Learning.

Trabajarás como analista de datos ambientales. Tu misión será transformar mediciones en una recomendación comprensible, reproducible y responsable.

---

## Reto integrador

**Pregunta guía:** ¿Podemos usar datos ambientales para identificar mediciones que requieren revisión y comunicar una recomendación confiable?

**Dataset:** `../datasets/mediciones_integrador.csv`

**Producto final:**

1. notebook ejecutado con análisis reproducible;
2. informe breve con hallazgos y limitaciones;
3. presentación docente o exposición final;
4. modelo de clasificación evaluado.

### Restricciones

- No modificar el dataset original.
- Documentar toda transformación.
- Separar datos de entrenamiento y prueba.
- No presentar correlación como causalidad.
- Explicar al menos un error del modelo.

---

## 1. Flujo del proyecto

```text
Pregunta
  ↓
Inspección y limpieza
  ↓
Análisis exploratorio
  ↓
Visualizaciones
  ↓
Modelo predictivo
  ↓
Evaluación
  ↓
Recomendación y límites
```

### Entregable mínimo

| Parte        | Evidencia                                         |
| ------------ | ------------------------------------------------- |
| Preparación  | tipos, faltantes y decisiones documentadas        |
| Exploración  | tabla resumen y tres gráficos                     |
| Modelo       | características, objetivo y separación train/test |
| Evaluación   | exactitud, reporte y matriz de confusión          |
| Comunicación | conclusión y limitaciones                         |

---

## 2. Fase 1: comprender el problema

Antes de abrir Pandas, responde:

- ¿Qué significa que una medición sea `revisar`?
- ¿Quién usaría la recomendación?
- ¿Qué error sería más costoso: no detectar una alerta o generar una alerta innecesaria?
- ¿Qué variables podrían influir y cuáles no están disponibles?

No confundas la etiqueta del dataset con una verdad universal. Es una decisión de referencia para practicar el flujo.

---

## 3. Fase 2: inspeccionar y limpiar

```python
import pandas as pd

ruta = "../datasets/mediciones_integrador.csv"
datos = pd.read_csv(ruta, parse_dates=["fecha"])

datos.info()
datos.isna().sum()
datos.describe(numeric_only=True)
```

Comprueba:

- número de filas y columnas;
- tipos de datos;
- duplicados;
- valores faltantes;
- distribución de `estado`;
- rangos plausibles.

Si encuentras un problema, registra el problema, la decisión y el efecto sobre el número de filas.

---

## 4. Fase 3: análisis exploratorio

Calcula, como mínimo:

- temperatura promedio por estación;
- humedad promedio por estación;
- cantidad de mediciones por estado;
- rango de precipitaciones;
- proporción de alertas por estación.

Ejemplo:

```python
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
```

---

## 5. Fase 4: construir la historia visual

Incluye tres gráficos:

1. barras de proporción de alertas por estación;
2. boxplot de temperatura por estado;
3. dispersión de temperatura y humedad, diferenciando el estado.

Cada gráfico debe tener:

- título que indique la pregunta;
- ejes y unidades;
- leyenda cuando sea necesaria;
- una observación escrita;
- una advertencia si el gráfico puede inducir a una interpretación incorrecta.

No incluyas gráficos que no cambien una decisión o comprensión.

---

## 6. Fase 5: entrenar y evaluar

Usa `temperatura`, `humedad` y `precipitacion_mm` como características iniciales. Usa `estado` como objetivo.

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

caracteristicas = ["temperatura", "humedad", "precipitacion_mm"]
X = datos[caracteristicas]
y = datos["estado"]

X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_entrenamiento, y_entrenamiento)
predicciones = modelo.predict(X_prueba)
```

Reporta:

- exactitud;
- precisión, recall y F1;
- matriz de confusión;
- número de ejemplos de prueba;
- qué error consideras más relevante.

Compara al menos dos configuraciones de `max_depth` y explica qué cambia.

---

## 7. Fase 6: informe y comunicación

Tu informe debe responder, sin párrafos extensos:

1. ¿Qué pregunta analizaste?
2. ¿Qué transformaciones aplicaste?
3. ¿Qué patrón principal encontraste?
4. ¿Qué modelo entrenaste?
5. ¿Cómo lo evaluaste?
6. ¿Qué recomendación propones?
7. ¿Qué limita tu conclusión?
8. ¿Qué dato recolectarías después?

Una buena conclusión diferencia tres niveles:

```text
Evidencia observada -> Interpretación prudente -> Acción propuesta
```

---

## Evaluación del proyecto

| Criterio                 | Peso | Evidencia                                   |
| ------------------------ | ---: | ------------------------------------------- |
| Comprensión del problema |  15% | pregunta, usuario y criterio de éxito       |
| Preparación de datos     |  20% | inspección y transformaciones reproducibles |
| Exploración visual       |  20% | tres gráficos interpretados                 |
| Modelo y evaluación      |  25% | separación, métricas y errores              |
| Comunicación             |  15% | informe y presentación claros               |
| Ética y límites          |   5% | sesgos, incertidumbre y próximos datos      |

### Lista de verificación

- [ ] El notebook se ejecuta de principio a fin.
- [ ] Las rutas funcionan desde la carpeta del notebook.
- [ ] El dataset central no fue modificado.
- [ ] Los gráficos tienen títulos, ejes y unidades.
- [ ] El modelo no usa `estado` como característica.
- [ ] La evaluación usa datos no vistos.
- [ ] El informe contiene una limitación concreta.
- [ ] La presentación permite entender la recomendación sin leer todo el código.
