import json
from tkinter import messagebox

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSpinBox, QPushButton, QHBoxLayout, QGroupBox

from Utiles.Titulo import Titulo


class TabConfiguraciones(QWidget):
    def __init__(self, tipo_fuente, tamano_fuente) -> None:
        super().__init__()

        self.lista_tipografias = self.retornarFuentes()  # Esto es para el combo box.
        self.tipo_fuente = tipo_fuente
        self.tamano_fuente = tamano_fuente

        # Agregamos algunas configuraciones a la ventana
        self.setFont(QFont(tipo_fuente, tamano_fuente))

        # Creamos el Layout Principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Creamos un Titulo para la Ventana
        titulo_ventana = Titulo("Configuraciones")
        self.layout_principal.addWidget(titulo_ventana)

        self.configuracionesFuenteTamano()

        frame_funciones = QGroupBox("Funciones")
        layout_funciones = QHBoxLayout()
        layout_funciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frame_funciones.setLayout(layout_funciones)

        boton_guardar_cambios = QPushButton("Guardar Cambios")
        boton_guardar_cambios.clicked.connect(self.guardarCambiosConfiguraciones)
        boton_guardar_cambios.setFixedSize(140, 40)
        layout_funciones.addWidget(boton_guardar_cambios)

        self.layout_principal.addWidget(frame_funciones)

        self.setLayout(self.layout_principal)

    def configuracionesFuenteTamano(self):
        frame_fuente_tamano = QGroupBox()
        layout_horizontal = QHBoxLayout()
        layout_horizontal.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frame_fuente_tamano.setLayout(layout_horizontal)

        layout_horizontal.addWidget(QLabel("Fuente:"))
        self.combo = QComboBox()
        self.combo.setFixedHeight(30)
        self.combo.addItems(self.lista_tipografias.split(","))
        self.combo.setCurrentText(self.tipo_fuente)
        layout_horizontal.addWidget(self.combo)

        layout_horizontal.addWidget(QLabel("Tamaño Fuente:"))
        self.spinbox = QSpinBox()
        self.spinbox.setFixedHeight(30)
        self.spinbox.setMinimum(1)
        self.spinbox.setMaximum(30)
        self.spinbox.setValue(self.tamano_fuente)
        layout_horizontal.addWidget(self.spinbox)

        self.layout_principal.addWidget(frame_fuente_tamano)

    def guardarCambiosConfiguraciones(self):
        if messagebox.askyesno("Advertencia", "¿Esta seguro de guardar los cambios?"):
            try:
                with open("Recursos/Configuraciones.json", "r") as archivo:
                    datos = json.load(archivo)

                datos["font"] = self.combo.currentText()
                datos["font-size"] = self.spinbox.text()

                with open("Recursos/Configuraciones.json", "w") as archivo:
                    json.dump(datos, archivo)
            except Exception as e:
                messagebox.showerror("Error", f"{e}")

    @staticmethod
    def retornarFuentes():
        with open("Recursos/Tipografias.txt") as tipografias:
            return tipografias.read()
