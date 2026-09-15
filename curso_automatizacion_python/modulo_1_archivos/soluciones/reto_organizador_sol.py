"""Solución docente del organizador de archivos."""

from pathlib import Path
import shutil


def organizar_archivos(carpeta: Path, modo_prueba: bool = True) -> list[tuple[Path, Path]]:
    """Planea o ejecuta movimientos sin sobrescribir archivos existentes."""
    movimientos = []
    if not carpeta.exists():
        return movimientos
    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue
        extension = archivo.suffix.lower().lstrip(".") or "sin_extension"
        destino_dir = carpeta / extension
        destino = destino_dir / archivo.name
        contador = 1
        while destino.exists():
            destino = destino_dir / \
                f"{archivo.stem}_{contador}{archivo.suffix}"
            contador += 1
        movimientos.append((archivo, destino))
        if not modo_prueba:
            destino_dir.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(destino))
    return movimientos
