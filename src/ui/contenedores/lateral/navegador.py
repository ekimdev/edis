# -*- coding: utf-8 -*-
# EDIS - a simple cross-platform IDE for C
#
# This file is part of EDIS
# Copyright 2014-2015 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

from PyQt4.QtGui import QListWidget

from src.ui.main import EDIS
from src.ui.contenedores.lateral import custom_dock


class Navegador(custom_dock.CustomDock):

    def __init__(self):
        custom_dock.CustomDock.__init__(self)
        self.navegador = QListWidget()
        self.setWidget(self.navegador)

        self.navegador.itemClicked.connect(self._cambiar_editor)

        EDIS.cargar_lateral("navegador", self)

    def agregar(self, archivo):
        self.navegador.addItem(archivo)

    def eliminar(self, indice):
        self.navegador.takeItem(indice)

    def cambiar_foco(self, indice):
        self.navegador.setCurrentRow(indice)

    def _cambiar_editor(self):
        indice = self.navegador.row(self.navegador.currentItem())
        principal = EDIS.componente("principal")
        principal.cambiar_widget(indice)


navegador = Navegador()