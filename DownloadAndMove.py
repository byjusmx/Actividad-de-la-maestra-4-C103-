import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/preet/Downloads"              # Agrega la ruta de tu carpeta "Descargas".
to_dir = "C:/Users/preet/Desktop/Downloaded_Files" #Crea una carpeta "Document_Files" en tu escritorio y actualiza la ruta correspondiente.


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Clase event handler

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Descargado " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("El Directorio Existe...")
                    print("Moviendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Creando Directorio...")
                    os.makedirs(path2)
                    print("Moviendo " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Inicia la clase event handler
event_handler = FileMovementHandler()

# Inicializa Observer
observer = Observer()

# Programa Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicia Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("¡detenido!")
    observer.stop()

