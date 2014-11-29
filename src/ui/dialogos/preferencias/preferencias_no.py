# -*- coding: utf-8 -*-
# EDIS - Entorno de Desarrollo Integrado Simple para C/C++
#
# This file is part of EDIS
# Copyright 2014 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

from collections import OrderedDict

from PyQt4.QtGui import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QComboBox,
    QPushButton,
    QStackedWidget
    )

from PyQt4.QtCore import (
    SIGNAL,
    Qt
    )

from src.ui.dialogos.preferencias import (
    preferencias_general,
    preferencias_editor,
    preferencias_gui,
    preferencias_compilacion
    )


class DialogoPreferencias(QDialog):

    def __init__(self, parent=None):
        super(DialogoPreferencias, self).__init__(parent)
        self.setWindowTitle(self.trUtf8("EDIS - Preferencias"))

        # Instancias de tabs
        self.general = preferencias_general.TabGeneral(self)
        self.editor = preferencias_editor.TabEditor()
        self.gui = preferencias_gui.TabGUI(self)
        self.compilacion = preferencias_compilacion.ECTab(self)

        # valor: texto en combo, clave: instancia de widgets
        self.widgets = OrderedDict([
            ('General', self.general),
            ('Editor', self.editor),
            ('GUI', self.gui),
            ('Compilador', self.compilacion)
            ])

        # Cargar interfaz
        self.cargar_gui()

        # Conexiones
        self.connect(self.combo, SIGNAL("currentIndexChanged(int)"),
            lambda: self.cambiar_widget(self.combo.currentIndex()))
        self.connect(self.botonCancelar, SIGNAL("clicked()"), self.close)
        self.connect(self.botonGuardar, SIGNAL("clicked()"), self._guardar)

    def cargar_gui(self):
        """ Carga todos los widgets en el QDialog """

        vLayout = QVBoxLayout(self)
        vLayout.setContentsMargins(0, 0, 0, 0)
        self.combo = QComboBox()
        vLayout.addWidget(self.combo)

        [self.combo.addItem(widget)
            for widget in list(self.widgets.keys())]

        self.stack = Stack()
        vLayout.addWidget(self.stack)

        [self.stack.addWidget(widget)
            for widget in list(self.widgets.values())]

        hLayout = QHBoxLayout()
        self.botonCancelar = QPushButton(self.trUtf8("Cancelar"))
        self.botonGuardar = QPushButton(self.trUtf8("Guardar"))
        layoutBotones = QGridLayout()
        hLayout.addWidget(self.botonCancelar)
        hLayout.addWidget(self.botonGuardar)
        layoutBotones.addLayout(hLayout, 0, 0, Qt.AlignLeft)
        vLayout.addLayout(layoutBotones)

    def cambiar_widget(self, indice):
        if not self.isVisible():
            self.show()
        self.stack.mostrar_widget(indice)

    def _guardar(self):
        """ Recorrer cada widget y sus tabs para guardar las configuraciones """

        [self.stack.widget(i).guardar()
            for i in range(self.combo.count())]
        self.close()


class Stack(QStackedWidget):

    def __init__(self):
        super(Stack, self).__init__()

    def setCurrentIndex(self, indice):
        QStackedWidget.setCurrentIndex(self, indice)

    def mostrar_widget(self, indice):
        self.setCurrentIndex(indice)