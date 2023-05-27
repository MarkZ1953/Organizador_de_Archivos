import os
import shutil
import json


class Organizador:
    def __init__(self, ruta_archivo, extensiones_documentos=(), extensiones_audio=(), extensiones_imagenes=(),
                 extensiones_videos=(), extensiones_otros=()) -> None:
        self.ruta_archivo = ruta_archivo

        self._extensiones_documentos = tuple(extensiones_documentos)
        self._entensiones_audio = tuple(extensiones_audio)
        self._extensiones_imagenes = tuple(extensiones_imagenes)
        self._extensiones_videos = tuple(extensiones_videos)
        self._extensiones_otros = tuple(extensiones_otros)

        self._nombre_carpetas = self.nombreCarpetas()
        self.comprobarCarpetas()
        self.moverArchivos()

    def comprobarCarpetas(self):
        for i in range(len(self._nombre_carpetas)):
            if os.path.exists(f"{self.ruta_archivo}/{self._nombre_carpetas[i]}"):
                continue
            else:
                os.mkdir(f"{self.ruta_archivo}/{self._nombre_carpetas[i]}")

    @staticmethod
    def nombreCarpetas():
        with open("Recursos/Nombre_Carpetas.json", "r") as archivo:
            datos = json.load(archivo)
        nombres = []
        for dato in datos.values():
            nombres.append(dato)
        return nombres

    def moverArchivos(self):
        documentos = []
        for file in os.listdir(self.ruta_archivo):
            if file.endswith(self._extensiones_documentos):
                documentos.append(file)
        for documento in documentos:
            shutil.move(f"{self.ruta_archivo}/{documento}", f"{self.ruta_archivo}/Documentos")


Organizador("E:/PRUEBA ARCHIVOS", (".pptx", ".docx"), (), (".jpg",), (".mp4", ".mkv"))
