# Módulo 3: Visualización y Análisis Exploratorio

## Introducción

Una visualización no es decoración: es una herramienta para encontrar patrones, comparar grupos y comunicar incertidumbre. En este módulo aprenderás a elegir un gráfico según la pregunta y a construir un análisis exploratorio reproducible.

Usarás **Matplotlib** para controlar cada elemento del gráfico y **Seaborn** para crear visualizaciones estadísticas claras con menos código.

---

## Reto del módulo

**Pregunta guía:** ¿Qué relación existe entre temperatura y humedad en las estaciones ambientales, y qué estación merece una revisión más detallada?

**Producto final:** un informe visual breve con tres gráficos, una conclusión respaldada por datos y una advertencia sobre los límites del análisis.

**Criterios de éxito:**

- elige un gráfico adecuado para cada pregunta;
- etiqueta ejes, unidades y título;
- compara estaciones sin ocultar diferencias;
- identifica patrones y valores atípicos;
- distingue correlación de causalidad;
- comunica una conclusión verificable.

---

## 1. Del dato a la historia visual

```text
Pregunta
   ↓
Variable y tipo de comparación
   ↓
Gráfico apropiado
   ↓
Patrón visible
   ↓
Comprobación numérica
   ↓
Conclusión con límites
```

Antes de graficar, pregunta:

1. ¿Quiero comparar categorías?
2. ¿Quiero observar una distribución?
3. ¿Quiero estudiar una relación entre dos variables?
4. ¿Quiero ver cambios en el tiempo?

---

## 2. Preparar el entorno y los datos

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
datos = pd.read_csv("../datasets/mediciones_ambientales.csv")
```

Una visualización reproducible debe indicar:

- origen del dataset;
- unidad de medida;
- columnas utilizadas;
- tratamiento de valores faltantes;
- semilla aleatoria, si existe muestreo.

Inspección inicial:

```python
datos.head()
datos.dtypes
datos.isna().sum()
datos.describe(numeric_only=True)
```

---

## 3. Elegir el gráfico

| Pregunta                                      | Gráfico recomendado  |
| --------------------------------------------- | -------------------- |
| ¿Qué estación tiene mayor promedio?           | barras               |
| ¿Cómo se distribuyen las temperaturas?        | histograma o boxplot |
| ¿Existe relación entre temperatura y humedad? | dispersión           |
| ¿Cómo cambia una variable en el tiempo?       | línea                |
| ¿Cómo se combinan dos categorías?             | barras agrupadas     |

Un gráfico debe responder una pregunta concreta. Evita añadir elementos que no aporten evidencia.

---

## 4. Matplotlib: control explícito

```python
promedios = datos.groupby("estacion", as_index=False)["temperatura"].mean()

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(promedios["estacion"], promedios["temperatura"], color="#2A788E")
ax.set_title("Temperatura promedio por estación")
ax.set_xlabel("Estación")
ax.set_ylabel("Temperatura (°C)")
plt.tight_layout()
plt.show()
```

Elementos mínimos:

- título informativo;
- ejes con unidades;
- escala legible;
- colores con significado consistente;
- fuente o nota metodológica cuando sea necesario.

Error frecuente: usar una escala recortada para exagerar diferencias. Revisa siempre los límites de los ejes.

---

## 5. Seaborn: relaciones y distribuciones

### Distribución por categoría

```python
fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=datos, x="estacion", y="temperatura", ax=ax, color="#7FB7BE")
ax.set_title("Distribución de temperatura por estación")
ax.set_xlabel("Estación")
ax.set_ylabel("Temperatura (°C)")
plt.tight_layout()
```

Un boxplot permite comparar mediana, dispersión y posibles valores atípicos. No muestra todos los puntos; combínalo con puntos individuales si el dataset es pequeño.

### Relación entre variables

```python
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(
    data=datos,
    x="temperatura",
    y="humedad",
    hue="estacion",
    style="estacion",
    s=90,
    ax=ax,
)
ax.set_title("Temperatura y humedad por estación")
ax.set_xlabel("Temperatura (°C)")
ax.set_ylabel("Humedad (%)")
plt.tight_layout()
```

El color debe representar una categoría clara. No uses una paleta solo porque sea llamativa.

---

## 6. Exploración: observar, medir, explicar

Una exploración responsable tiene tres niveles:

| Nivel       | Pregunta                                           |
| ----------- | -------------------------------------------------- |
| Observación | ¿Qué patrón aparece en el gráfico?                 |
| Medición    | ¿Qué promedio, rango o correlación lo respalda?    |
| Explicación | ¿Qué hipótesis podría explicarlo y qué dato falta? |

### Correlación

```python
correlacion = datos[["temperatura", "humedad"]].corr().loc[
    "temperatura", "humedad"
]
```

Una correlación cercana a `1` o `-1` indica asociación lineal, pero no demuestra causalidad. Puede haber variables no observadas, sesgos de medición o muy pocos datos.

### Valores atípicos

Un valor atípico no debe eliminarse automáticamente. Primero pregunta:

- ¿es un error de captura?
- ¿es una medición real pero poco frecuente?
- ¿cambia la conclusión?
- ¿hay suficiente evidencia para investigarlo?

---

## 7. Diseño visual responsable

- Usa una paleta legible y consistente.
- No codifiques información solo con color.
- Redondea valores sin ocultar diferencias relevantes.
- Ordena categorías cuando facilite la comparación.
- Evita gráficos 3D si una vista plana responde mejor.
- Escribe la conclusión debajo o junto al gráfico, no dentro de una leyenda confusa.
- Conserva el código para que otra persona pueda reproducir la figura.

---

## 8. Actividad del estudiante

Abre `01_visualizacion_exploratoria.ipynb` y completa `02_reto_visualizacion.py`.

### Reto 1: reproducción

Crea un gráfico de barras con la temperatura promedio por estación.

### Reto 2: comparación

Crea un boxplot de temperatura por estación y describe la dispersión.

### Reto 3: extensión

Crea un gráfico de dispersión de temperatura frente a humedad, calcula la correlación y escribe una conclusión de dos líneas con una limitación.

---

## Evidencia y evaluación

| Criterio       | Logrado cuando...                               |
| -------------- | ----------------------------------------------- |
| Elección       | el gráfico responde a una pregunta concreta     |
| Técnica        | el código se ejecuta y usa etiquetas completas  |
| Exploración    | comparas distribución, centro y dispersión      |
| Interpretación | separas observación de explicación              |
| Comunicación   | la conclusión cita evidencia visible o numérica |
| Ética          | reconoces límites, sesgos o incertidumbre       |

### Reflexión final

1. ¿Qué diferencia comunica un boxplot que no comunica un promedio aislado?
2. ¿Por qué correlación no significa causalidad?
3. ¿Qué gráfico cambiarías si el número de estaciones se multiplicara por diez?
