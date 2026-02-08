from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time 

from filetype import filetype
from downloadWait import aguardar_conclusao
from folderManagement import criaPastas, moveFiles


# Roda o script que cria as pastas
criaPastas()

# Classe do watchdog para monitorar os arquivos quando entrarem em Downloads
class MeuHandler(FileSystemEventHandler):
    # Função "on_moved" para monitorar os arquivos que forem renomeados ou seja foram instalados 
    def on_moved(self, event):
        if not event.is_directory:
            if not event.dest_path.endswith(('.crdownload', '.part', '.tmp')):
                if aguardar_conclusao(event.dest_path):
                    arquivo = Path(event.dest_path).name
                    categoria_arquivo, tipo_arquivo = filetype(arquivo)
                    moveFiles(event.dest_path, tipo_arquivo)
                    print(f"O arquivo {event.dest_path} foi instalado e movido.")
                else:
                    print("Download Falhou")

    # Função "on_created" para monitorar os arquivos que forem movidos para a pasta de downloads ou forem baixados 
    def on_created(self, event):
        if not event.is_directory:
            if not event.src_path.endswith(('.crdownload', '.part', '.tmp')):
                if aguardar_conclusao(event.src_path):
                    arquivo = Path(event.src_path).name
                    categoria_arquivo, tipo_arquivo = filetype(arquivo)
                    moveFiles(event.src_path, tipo_arquivo)
                    print(f"O arquivo {event.src_path} foi instalado e movido.")
                else:
                    print("Download Falhou")


path = Path.home() / "Downloads"
event_handler = MeuHandler()
observer = Observer()
observer.schedule(event_handler, str(path), recursive=False)

# Loop do watchdog
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()