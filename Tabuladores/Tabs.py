from PySide6.QtWidgets import QTabWidget

from Tabuladores.TabConfiguraciones import TabConfiguraciones
from Tabuladores.TabOpciones import TabOpciones


class Tabs(QTabWidget):
    def __init__(self):
        super().__init__()

        # Creamos las Pestañas
        self.tab_opciones = TabOpciones()
        # self.tab_configuraciones = TabConfiguraciones()

        # Agregamos las Pestañas al TabPrincipal
        self.addTab(self.tab_opciones, "Principal")
