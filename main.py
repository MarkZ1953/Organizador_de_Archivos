import json
from tkinter import Frame, Tk, messagebox
from tkinter.ttk import (Button, Combobox, Label, Notebook, Spinbox)

from PySide6.QtWidgets import QMainWindow, QApplication

from Tabuladores.TabOpciones import TabOpciones
from Tabuladores.Tabs import Tabs


class VentanaPrincipal(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Extraemos las configuraciones de los Archivos JSON
        self.tipografia_widgets = self.configuracion_fuente_widgets()  # Fuente predeterminada : Minecraft.
        self.tamano_tipografia = self.configuracion_tamanofuente_widgets()  # Tamaño predeterminado de los textos : 10
        self.lista_tipografias = self.listar_fuentes()  # Esto es para el combo box.

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Organizador de Archivos")
        self.resize(600, 600)

        self.setCentralWidget(Tabs())

    def crear_widgets(self):
        self.frame1 = Frame(self.tabulador2)
        self.frame1.grid(row=0, column=0)

        Label(self.frame1, text="Fuente : ", font=(self.tipografia_widgets, self.tamano_tipografia)).grid(row=0,
                                                                                                          column=0)
        self.combo = Combobox(self.frame1, values=self.lista_tipografias.split(","), state="readonly", width=30)
        self.combo.set(self.configuracion_fuente_widgets())
        self.combo.grid(row=0, column=1, pady=30)

        Label(self.frame1, text="Tamaño Fuente : ", font=(self.tipografia_widgets, self.tamano_tipografia)).grid(row=0,
                                                                                                                 column=2,
                                                                                                                 pady=10)
        self.spinbox = Spinbox(self.frame1, from_=1, to=30, wrap=True)
        self.spinbox.set(self.tamano_tipografia)
        self.spinbox.grid(row=0, column=3)

        Button(self.tabulador2, text="Guardar Cambios", cursor="hand2", command=lambda: self.guardar_cambios(),
               width=30).grid(row=1, column=0, sticky="ns", pady=10)

    @staticmethod
    def configuracion_fuente_widgets():
        with open("Recursos/Configuraciones.json") as archivo:
            configuraciones = json.load(archivo)
            return configuraciones["font"]

    @staticmethod
    def listar_fuentes():
        with open("Recursos/Tipografias.txt") as tipografias:
            return tipografias.read()

    def guardar_cambios(self):
        if messagebox.askyesno("Advertencia", "¿Esta seguro de guardar los cambios?"):
            try:
                with open("Recursos/Configuraciones.json", "r") as archivo:
                    datos = json.load(archivo)
                datos["font"] = self.combo.get()
                datos["font-size"] = self.spinbox.get()
                with open("Recursos/Configuraciones.json", "w") as archivo:
                    json.dump(datos, archivo)
            except Exception as e:
                messagebox.showerror("Error", f"{e}")

    @staticmethod
    def configuracion_tamanofuente_widgets():
        with open("Recursos/Configuraciones.json") as archivo:
            configuraciones = json.load(archivo)
            return configuraciones["font-size"]


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
