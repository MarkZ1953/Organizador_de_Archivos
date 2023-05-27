import json
from tkinter import Frame, messagebox
from tkinter.ttk import (Button, Combobox, Label, Spinbox)

from PySide6.QtWidgets import QMainWindow, QApplication

from Tabuladores.Tabs import Tabs


class VentanaPrincipal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Extraemos las configuraciones de los Archivos JSON
        self.tipo_fuente = self.retornarConfiguracionTipoFuente()  # Fuente predeterminada : Minecraft.
        self.tamano_fuente = self.retornarConfiguracionTamanoFuente()  # Tamaño predeterminado de los textos : 10

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Organizador de Archivos")
        self.resize(600, 600)

        self.setCentralWidget(Tabs(self.tipo_fuente, self.tamano_fuente))

    @staticmethod
    def retornarConfiguracionTipoFuente():
        with open("Recursos/Configuraciones.json") as archivo:
            configuraciones = json.load(archivo)
            return configuraciones["font"]

    @staticmethod
    def retornarConfiguracionTamanoFuente():
        with open("Recursos/Configuraciones.json") as archivo:
            configuraciones = json.load(archivo)
            return configuraciones["font-size"]


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
