import json
from tkinter import filedialog, messagebox

from PySide6.QtGui import Qt
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QGridLayout, QCheckBox,
                               QTextEdit)

from Utiles.Titulo import Titulo


class TabOpciones(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Declaramos las listas
        self.check_box_documentos = []
        self.check_box_videos = []
        self.check_box_imagenes = []
        self.check_box_audios = []
        self.check_box_compresiones = []

        # Extraemos las configuraciones de los Archivos JSON
        self.extensiones_documentos, self.extensiones_imagenes, self.extensiones_videos, self.extensiones_audios, \
            self.extensiones_compresiones = self.extensiones_archivos()

        # Creamos el Layout Principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.setAlignment(Qt.AlignmentFlag.AlignTop)

        # self.tipografia_widgets = tipografia_widgets
        # self.tabulador_principal = tabulador_principal
        self.ruta_carpeta = None

        # Creamos un Titulo para la Ventana
        titulo_ventana = Titulo("Organizador de Archivos")
        self.layout_principal.addWidget(titulo_ventana)

        self.crearCajaRuta()
        self.crearCheckButtons()
        self.crearBotones()

        self.setLayout(self.layout_principal)

    def crearBotones(self):

        frame_funciones = QGroupBox("Funciones")
        layout_funciones = QHBoxLayout()
        frame_funciones.setLayout(layout_funciones)

        boton_agregar_ruta = QPushButton(text="Añadir Ruta")
        boton_agregar_ruta.setFixedSize(140, 40)
        boton_agregar_ruta.clicked.connect(lambda: self.abrir_directorio())

        boton_organizar = QPushButton(text="Organizar")
        boton_organizar.setFixedSize(140, 40)
        boton_organizar.clicked.connect(lambda: self.organizarArchivos())

        layout_funciones.addWidget(boton_agregar_ruta)
        layout_funciones.addWidget(boton_organizar)

        self.layout_principal.addWidget(frame_funciones)

    @staticmethod
    def extensiones_archivos():
        with open("Recursos/Extensiones.json", "r") as archivo:
            datos = json.load(archivo)
        return datos["docs"], datos["images"], datos["audio"], datos["video"], datos["compression"]

    def crearCheckButtons(self):

        frame_extensiones = QGroupBox("Extensiones")
        layout_extensiones = QGridLayout()
        frame_extensiones.setLayout(layout_extensiones)

        for i in range(len(self.extensiones_documentos)):
            check_box = QCheckBox()
            check_box.setText(self.extensiones_documentos[i])
            layout_extensiones.addWidget(check_box, i, 0)
            self.check_box_documentos.append(check_box)

        for i in range(len(self.extensiones_imagenes)):
            check_box = QCheckBox()
            check_box.setText(self.extensiones_imagenes[i])
            layout_extensiones.addWidget(check_box, i, 1)
            self.check_box_imagenes.append(check_box)

        for i in range(len(self.extensiones_videos)):
            check_box = QCheckBox()
            check_box.setText(self.extensiones_videos[i])
            layout_extensiones.addWidget(check_box, i, 2)
            self.check_box_videos.append(check_box)

        for i in range(len(self.extensiones_audios)):
            check_box = QCheckBox()
            check_box.setText(self.extensiones_videos[i])
            layout_extensiones.addWidget(check_box, i, 3)
            self.check_box_audios.append(check_box)

        for i in range(len(self.extensiones_compresiones)):
            check_box = QCheckBox()
            check_box.setText(self.extensiones_compresiones[i])
            layout_extensiones.addWidget(check_box, i, 4)
            self.check_box_compresiones.append(check_box)

        self.layout_principal.addWidget(frame_extensiones)

    def abrir_directorio(self):
        self.ruta_carpeta = filedialog.askdirectory(title="Buscar Ruta", initialdir="Desktop")

        if self.ruta_carpeta:
            self.caja_texto_ruta.config(state="normal")
            self.caja_texto_ruta.delete(1.0, "end")
            self.caja_texto_ruta.insert(1.0, "Ruta : " + self.ruta_carpeta)
            self.caja_texto_ruta.config(state="disable")

    def crearCajaRuta(self):
        self.caja_texto_ruta = QTextEdit()
        self.caja_texto_ruta.setFixedHeight(100)
        self.layout_principal.addWidget(self.caja_texto_ruta)

    def organizarArchivos(self):
        if messagebox.askyesno("Advertencia", "Esta seguro que desea continuar?"):
            # if self.ruta_carpeta is not None:
            print(self.seleccionarExtensiones())
            # Organizador(self.ruta_carpeta)
        else:
            messagebox.showerror("Error", "Debes seleccionar una ruta")

    def seleccionarExtensiones(self):

        lista_documentos = []
        lista_imagenes = []
        lista_audio = []
        lista_videos = []
        lista_compresiones = []

        for check_box in self.check_box_documentos:
            if check_box.isChecked():
                lista_documentos.append(check_box.text())

        for check_box in self.check_box_imagenes:
            if check_box.isChecked():
                lista_imagenes.append(check_box.text())

        for check_box in self.check_box_audios:
            if check_box.isChecked():
                lista_audio.append(check_box.text())

        for check_box in self.check_box_videos:
            if check_box.isChecked():
                lista_videos.append(check_box.text())

        for check_box in self.check_box_compresiones:
            if check_box.isChecked():
                lista_compresiones.append(check_box.text())

        return lista_documentos, lista_imagenes, lista_audio, lista_videos, lista_compresiones
