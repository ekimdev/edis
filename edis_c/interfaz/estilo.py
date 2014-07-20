#-*- coding: utf8 -*-

from PyQt4.QtGui import QPlainTextEdit
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QLabel

from edis_c.interfaz import tabitem


class EstiloDeCodigo(QPlainTextEdit, tabitem.TabItem):

    def __init__(self):
        super(EstiloDeCodigo, self).__init__()
        tabitem.TabItem.__init__(self)
        self.setReadOnly(True)
        self.setStyleSheet("color: #666")
        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.addWidget(QLabel(
            self.trUtf8("<h1>Estilos de código para C</h1>")))
        layout.addWidget(QLabel(
            self.trUtf8("Algunas convenciones o estándares para escribir"
            " código en C.")))
        layout.addWidget(QLabel(
            self.trUtf8("<b>Líneas</b><br>Con una sola instrucción por línea"
            " el código quedaría más legible.<br>\twhile")))
        self.setLayout(layout)