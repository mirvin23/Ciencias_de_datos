# Módulo 4: Control de Interfaz Gráfica y Tareas Programadas

## Reto

Diseñar un bot visible que abra una aplicación autorizada, realice una secuencia de clics, envíe un mensaje de prueba y se ejecute según una programación.

## Librerías

- `pyautogui`: teclado, ratón y capturas.
- `schedule`: definir tareas periódicas.
- `time`: pausas controladas.

## Principios de seguridad

- Automatiza solo aplicaciones y cuentas autorizadas.
- Usa `pyautogui.PAUSE` y una tecla de emergencia.
- Prueba primero con una aplicación de demostración.
- No automatices credenciales, pagos ni mensajes masivos.
- Incluye `modo_prueba` y registro de eventos.
- Una tarea programada debe poder cancelarse.

## Flujo

```text
Definir tarea -> modo de prueba -> ejecutar una vez -> programar -> supervisar -> cancelar
```

## Ejemplo

```python
import pyautogui
import schedule

pyautogui.PAUSE = 0.5

def tarea_demo():
    print("Tarea ejecutada")

schedule.every().day.at("09:00").do(tarea_demo)
```

No mantengas un bucle infinito durante las primeras pruebas. Ejecuta una vez, valida y añade la programación al final.

## Entrega

El bot debe separar la lógica de negocio de las acciones de interfaz, permitir simulación y documentar cómo cancelar el proceso.

## Evaluación

- seguridad y cancelación: 30%; diseño de tarea: 25%; programación: 20%; registro y documentación: 25%.
