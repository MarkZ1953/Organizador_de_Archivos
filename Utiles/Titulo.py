from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QFrame, QLabel


class Titulo(QFrame):
    def __init__(self, titulo_ventana: str):
        super().__init__()

        # Agregamos algunas configuraciones al Frame
        self.setFixedHeight(80)
        self.setStyleSheet("background-color: rgb(15, 44, 115);")

        layout_titulo = QHBoxLayout()

        titulo = QLabel(titulo_ventana)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFont(QFont("Roboto", 20, QFont.Bold))
        titulo.setStyleSheet("color: white;")

        layout_titulo.addWidget(titulo)

        self.setLayout(layout_titulo)
