"""Reto del estudiante: organizar archivos por extensión."""

from pathlib import Path


def organizar_archivos(carpeta: Path, modo_prueba: bool = True) -> list[tuple[Path, Path]]:
    """Organiza archivos de una carpeta y devuelve los movimientos planeados.

    Con modo_prueba=True no modifica el sistema de archivos.
    """
    # PENDIENTE 1: lista solo archivos de la carpeta, sin recorrer subcarpetas.
    # PENDIENTE 2: calcula una carpeta destino basada en la extensión.
    # PENDIENTE 3: crea destinos solo cuando modo_prueba sea False.
    # PENDIENTE 4: evita sobrescribir archivos existentes.
    raise NotImplementedError(
        "Completa organizar_archivos como parte del reto")


if __name__ == "__main__":
    carpeta_prueba = Path("carpeta_prueba")
    print(
        "Plantilla lista. Crea una carpeta de prueba y completa "
        "organizar_archivos antes de ejecutar los casos."
    )
