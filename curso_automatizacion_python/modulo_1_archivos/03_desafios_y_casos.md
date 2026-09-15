# Módulo 1: desafíos y casos de uso

## Cómo trabajar

Resuelve los desafíos en orden. Usa siempre una carpeta temporal y conserva el modo de prueba hasta que puedas explicar cada movimiento.

---

## Desafío 1: explorador de archivos

### Situación

Una persona necesita saber qué hay en una carpeta sin abrir cada archivo.

### Tarea

Crea `inventario(carpeta)` que devuelva una lista de diccionarios con:

- `nombre`;
- `extension`;
- `tamanio_bytes`;
- `es_archivo`.

### Pista

Usa `iterdir()`, `is_file()`, `name`, `suffix` y `stat().st_size`.

### Criterio

La función no debe modificar la carpeta y debe ignorar subcarpetas o marcarlas claramente.

---

## Desafío 2: clasificador por categoría

### Situación

Separar por extensión funciona, pero las personas prefieren carpetas con significado.

### Tarea

Implementa `categoria_para(extension)` con estas reglas:

| Categoría    | Extensiones         |
| ------------ | ------------------- |
| `imagenes`   | jpg, jpeg, png, gif |
| `documentos` | pdf, docx, txt      |
| `datos`      | csv, xlsx, json     |
| `otros`      | cualquier otra      |

### Casos de prueba

```python
assert categoria_para("JPG") == "imagenes"
assert categoria_para("csv") == "datos"
assert categoria_para("zip") == "otros"
```

---

## Desafío 3: planificador sin efectos

### Situación

Antes de mover archivos, el usuario necesita revisar la propuesta.

### Tarea

Crea `planificar_movimientos(carpeta, raiz_destino)` que devuelva pares `(origen, destino)` sin crear carpetas ni mover archivos.

### Criterio

Después de llamar a la función, la lista de archivos originales debe ser idéntica.

---

## Desafío 4: colisiones

### Situación

Ya existe `documentos/informe.pdf` y llega otro archivo con el mismo nombre.

### Tarea

Genera un nombre alternativo:

```text
informe.pdf
informe_1.pdf
informe_2.pdf
```

No reemplaces el archivo existente.

---

## Desafío 5: organizador seguro

### Situación

Ya puedes planificar movimientos y resolver colisiones.

### Tarea

Completa `02_reto_organizador.py` para que:

1. acepte una carpeta;
2. procese solo archivos inmediatos;
3. clasifique por extensión;
4. devuelva el plan en modo de prueba;
5. cree destinos y mueva solo con `modo_prueba=False`;
6. informe cuántos archivos procesó.

### Casos de prueba mínimos

- archivo con extensión `.PDF`;
- archivo sin extensión;
- subcarpeta que no debe ser recorrida;
- destino ya existente;
- carpeta inexistente.

---

## Desafío 6: auditoría

### Situación

Un equipo necesita saber qué ocurrió durante la automatización.

### Tarea

Registra cada operación en `registro_movimientos.csv` con:

- fecha y hora;
- archivo origen;
- archivo destino;
- estado: `planificado`, `movido` o `error`;
- mensaje de error, si existe.

No registres contenido de archivos ni datos privados innecesarios.

---

## Casos de uso para discutir

### Oficina

Organizar facturas, contratos y hojas de cálculo recibidas durante una semana.

**Pregunta:** ¿qué archivos no deberían moverse automáticamente?

### Fotografía

Separar imágenes por extensión y conservar archivos RAW en una categoría especial.

**Pregunta:** ¿por qué una extensión no siempre describe el contenido real?

### Datos

Separar CSV y JSON para un pipeline de análisis.

**Pregunta:** ¿qué validación harías antes de mover un archivo que el pipeline necesita?

### Respaldo

Copiar, no mover, archivos importantes antes de una limpieza.

**Pregunta:** ¿cómo demostrarías que la copia se completó?

---

## Rúbrica del desafío final

| Nivel         | Descripción                                                        |
| ------------- | ------------------------------------------------------------------ |
| Inicial       | lista archivos, pero mezcla rutas o modifica sin avisar            |
| En desarrollo | clasifica y planifica, pero no controla colisiones                 |
| Logrado       | simula, valida, evita sobrescritura y ejecuta en carpeta de prueba |
| Sobresaliente | registra resultados, maneja errores y explica límites              |
