from pathlib import Path
import shutil

home = Path.home()

# Destinos de cada arquivo

destinos = {
    "pdf": home / "Documents" ,
    "docx": home / "Documents" ,        
    "txt": home / "Documents" ,
    "xlsx": home / "Documents",

    "png": home / "Pictures" / "Midias",
    "jpg": home / "Pictures" / "Midias",
    "jpeg": home / "Pictures" / "Midias",
    "mp3": home / "Pictures" / "Midias",
    "mp4": home / "Pictures" / "Midias",
    "mov": home / "Pictures" / "Midias",
    "webp": home / "Pictures" / "Midias",

    "exe": home / "Downloads" / "Instaladores",
    "msi": home / "Downloads" / "Instaladores",

    "zip": home / "Downloads" / "Compactados",
    "rar": home / "Downloads" / "Compactados",
    }

def criaPastas():
    # Lógica para criar as pastas se elas não existirem
    for pasta in destinos.values():
        pasta.mkdir(parents=True, exist_ok=True)

def moveFiles(filePath, categoria):
    if categoria in destinos:
        shutil.move(filePath, destinos[categoria])
    else:
        return 0