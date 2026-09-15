---
name: curso-datos-steam
description: "Diseñar módulos y materiales de cursos STEAM de programación para Ciencia de Datos con Aprendizaje Basado en Proyectos (ABP), pensamiento computacional y retos prácticos. Usar cuando se soliciten módulos, cuadernos de estudio, diapositivas Marp, notebooks Jupyter, scripts, soluciones docentes o secuencias didácticas de Python, NumPy, Pandas, Matplotlib, Seaborn o Scikit-Learn."
argument-hint: "Indica el módulo, nivel, duración y producto final del proyecto"
user-invocable: true
disable-model-invocation: false
---

# Curso de Datos STEAM

## Propósito

Crear materiales listos para el flujo de trabajo docente y del estudiante en cursos de programación orientados a Ciencia de Datos. La experiencia debe priorizar aprender haciendo, pensamiento computacional, resolución de retos y productos verificables.

## Cuándo usar

- Diseñar o desarrollar uno de los módulos del curso activo.
- Convertir un reto de Ciencia de Datos en una secuencia ABP.
- Generar cuadernos para PDF, presentaciones Marp, notebooks, scripts o soluciones.
- Adaptar una actividad a un nivel, duración, dataset o producto final concreto.
- Revisar si un módulo es ejecutable, coherente y útil para docente y estudiante.

## Curso activo

1. **Módulo 1:** Fundamentos de Python y lógica algorítmica.
2. **Módulo 2:** Manipulación y análisis de datos con NumPy y Pandas.
3. **Módulo 3:** Visualización y análisis exploratorio con Matplotlib y Seaborn.
4. **Módulo 4:** Fundamentos de Machine Learning con Scikit-Learn.

## Procedimiento

### 1. Precisar el encargo

Extrae o solicita, si falta, estos datos:

- módulo y tema;
- nivel previo del estudiante;
- duración y número de sesiones;
- producto o evidencia final;
- dataset, contexto científico o problema auténtico;
- entorno de ejecución y dependencias;
- idioma y formato de entrega.

Si faltan datos no bloqueantes, declara supuestos breves y continúa. Si falta el producto final o el nivel, formula una pregunta antes de diseñar actividades que dependan de ellos.

### 2. Convertir el tema en reto ABP

Define en una frase:

- **situación:** contexto científico, social o tecnológico;
- **pregunta guía:** qué debe descubrir, construir o decidir el estudiante;
- **producto final:** notebook, informe, visualización, modelo o presentación;
- **criterios de éxito:** evidencia observable y medible.

Conecta cada concepto con una decisión del proyecto. Evita ejercicios aislados salvo que preparen directamente una parte del producto.

### 3. Diseñar la progresión algorítmica

Antes del código, presenta una secuencia visual y breve:

`Problema -> Datos/entradas -> Transformaciones -> Decisiones -> Salida -> Validación`

Descompón el reto en pasos pequeños. Para cada paso indica entradas, operación, salida esperada y una comprobación sencilla. Introduce la solución gradualmente: primero razonamiento, después pseudocódigo, luego código parcial y finalmente extensión opcional.

### 4. Respetar la estructura del curso

Mantén siempre esta estructura raíz, salvo que el usuario solicite explícitamente otra:

```text
/curso_data_science
├── /modulo_1_fundamentos
│   ├── 00_guia_del_modulo.md
│   ├── 01_estructuras_y_flujo.ipynb
│   ├── 02_reto_algoritmico.py
│   └── /soluciones
│       └── reto_algoritmico_sol.py
├── /modulo_2_manipulacion
└── /datasets
```

Reglas de organización:

- El contenido de cada módulo vive dentro de su propia carpeta.
- `datasets` es la carpeta central para los CSV y no se duplican datasets dentro de los módulos.
- Las soluciones docentes viven exclusivamente en la subcarpeta `soluciones` del módulo correspondiente.
- Conserva los nombres de archivo establecidos para el Módulo 1.
- Para módulos posteriores usa la misma convención numérica y semántica, por ejemplo `00_guia_del_modulo.md`, un notebook de práctica, un reto del estudiante y una subcarpeta `soluciones`.
- Crea solo las carpetas y archivos solicitados; no inventes entregables adicionales.

### 5. Generar los entregables

Cuando se solicite el Módulo 1 completo, genera exactamente estos archivos:

1. **`modulo_1_fundamentos/00_guia_del_modulo.md`**
   - Markdown limpio y exportable a PDF.
   - Objetivos, reto, conceptos mínimos, proceso paso a paso, ejemplos, tablas y evaluación.
   - Usa `---` como salto de página.
   - Explica cada bloque de código con propósito, entrada, salida y error frecuente.
   - Incluye retos graduados y criterios de entrega.

2. **Presentaciones docentes**
   - Compatible con Marp.
   - Comienza con `marp: true` y, cuando sea útil, directivas de tema o tamaño.
   - Una idea por diapositiva, viñetas cortas y palabras clave.
   - Usa diagramas simples en Mermaid o ASCII cuando aclaren el flujo.
   - No incluyas párrafos densos ni soluciones completas del estudiante.
   - Guarda la presentación dentro de la carpeta del módulo cuando sea solicitada; usa un nombre descriptivo como `03_presentacion_docente.md`.

3. **`modulo_1_fundamentos/01_estructuras_y_flujo.ipynb`**
   - Código ejecutable y dependencias explícitas.
   - Docstrings en funciones y comentarios mínimos.
   - Secciones de preparación, ejemplo guiado, reto y reflexión.
   - Deja los espacios de implementación como `# TODO: Tu código aquí`.
   - En notebooks, conserva JSON válido y estructura `.ipynb`: cada celda es un objeto con `cell_type`, `metadata` y `source`; toda celda nueva debe incluir `metadata.language` (`markdown` o `python`). Las celdas existentes deben conservar `metadata.id` único. Usa una lista de cadenas en `source` y escapa correctamente comillas, saltos de línea y barras.

4. **`modulo_1_fundamentos/02_reto_algoritmico.py`**
   - Archivo base para el estudiante.
   - Incluye docstrings, instrucciones y espacios `# TODO: Tu código aquí`.
   - No contiene la implementación final.

5. **`modulo_1_fundamentos/soluciones/reto_algoritmico_sol.py`**
   - Soluciones separadas y claramente marcadas como material docente.
   - Incluye una solución funcional y, si aporta valor, una alternativa razonada.
   - No mezcles respuestas docentes en el cuaderno del estudiante.

Si el usuario pide solo un entregable, genera únicamente el archivo solicitado en su ubicación canónica y conserva la misma progresión didáctica. Para módulos posteriores, sustituye el prefijo por la carpeta correspondiente, por ejemplo `modulo_2_manipulacion/`.

### 6. Aplicar reglas de estilo

- Escribe en español claro, directo y accionable.
- Mantén las explicaciones ultra-concisas, visuales y prácticas.
- Usa nombres de variables descriptivos y evita código mágico.
- Prefiere librerías estándar del módulo y APIs conocidas.
- No inventes datos científicos: declara datasets sintéticos o fuentes requeridas.
- Distingue con claridad contenido del estudiante y material exclusivo del docente.
- Haz accesible el material: instrucciones numeradas, salidas esperadas y errores frecuentes.

### 7. Verificar antes de entregar

Comprueba:

- frontmatter válido solo en la skill, sin claves ambiguas ni YAML roto;
- estructura raíz, carpetas y nombres canónicos respetados;
- soluciones ubicadas dentro de `soluciones` y datasets referenciados desde `datasets`;
- archivos con nombres consistentes y referencias internas correctas;
- notebook parseable como JSON y con `metadata.language` en cada celda;
- imports, rutas de archivos y dependencias documentados;
- retos resolubles con los conceptos enseñados;
- soluciones que ejecutan y corresponden a cada reto;
- separación real entre estudiante y docente;
- criterios de evaluación observables;
- ausencia de párrafos densos en las diapositivas y de saltos de lógica en el cuaderno.

Ejecuta la comprobación más barata disponible: parsea el notebook como JSON, compila el script o ejecuta las celdas de preparación y solución. Si no es posible ejecutar, informa qué quedó sin verificar.

## Plantilla mínima de módulo

```text
Título y contexto
Pregunta guía
Producto final
Objetivos observables
Mapa Problema -> Datos -> Proceso -> Decisión -> Resultado
Conceptos mínimos
Ejemplo guiado
Reto 1: reproducción
Reto 2: adaptación
Reto 3: extensión
Evidencia y rúbrica breve
Reflexión final
```

## Resultado esperado

Entrega archivos completos, autocontenidos y listos para integrarse en el curso. Al finalizar, resume qué produce cada archivo, qué supuestos adoptaste y qué validaciones ejecutaste. Si el encargo es ambiguo, señala la decisión que más afecta al diseño y pide una sola aclaración concreta para la siguiente iteración.
