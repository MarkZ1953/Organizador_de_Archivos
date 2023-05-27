from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTabWidget

from Tabuladores.TabConfiguraciones import TabConfiguraciones
from Tabuladores.TabOpciones import TabOpciones


class Tabs(QTabWidget):
    def __init__(self, tipo_fuente, tamano_fuente):
        super().__init__()

        # Agregamos algunas configuraciones a la ventana
        self.setFont(QFont(tipo_fuente, tamano_fuente))

        # Creamos las Pestañas
        self.tab_opciones = TabOpciones(tipo_fuente, tamano_fuente)
        self.tab_configuraciones = TabConfiguraciones(tipo_fuente, tamano_fuente)

        # Agregamos las Pestañas al TabPrincipal
        self.addTab(self.tab_opciones, "Principal")
        self.addTab(self.tab_configuraciones, "Configuraciones")
