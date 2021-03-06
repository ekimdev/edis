# -*- coding: utf-8 -*-
# EDIS - a simple cross-platform IDE for C
#
# This file is part of EDIS
# Copyright 2014-2015 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

import re
import os
from datetime import datetime

from PyQt4.QtGui import (
    QDialog,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton
    )

from PyQt4.QtCore import (
    Qt,
    QFile
    )


class FileProperty(QDialog):

    def __init__(self, editor, parent=None):
        QDialog.__init__(self, parent, Qt.Dialog)
        self.setWindowTitle(self.trUtf8("Propiedades del archivo"))
        filename = editor.nombre
        vLayout = QVBoxLayout(self)
        vLayout.setContentsMargins(10, 15, 10, 10)
        vLayout.setSpacing(10)

        lbl_title = QLabel(self.trUtf8("{0}").format(filename.split('/')[-1]))
        lbl_title.setStyleSheet("font-weight: bold; font-size: 24px;")
        vLayout.addWidget(lbl_title)

        grid = QGridLayout()
        grid.addWidget(QLabel(self.trUtf8("<b>Tipo:</b>")), 1, 0)
        grid.addWidget(QLabel(self.get_type(filename)), 1, 1)
        grid.addWidget(QLabel(self.trUtf8("<b>Tamaño:</b>")), 2, 0)
        grid.addWidget(QLabel(self.get_size(filename)), 2, 1)
        grid.addWidget(QLabel(self.trUtf8("<b>Ubicación:</b>")), 3, 0)
        grid.addWidget(QLabel(filename), 3, 1)
        grid.addWidget(QLabel(self.trUtf8("<b>Líneas de código:</b>")), 4, 0)
        grid.addWidget(QLabel(self.tr("{0}").format(editor.lineas -
                       len(self.get_comment_spaces(editor)))), 4, 1)
        grid.addWidget(QLabel(
            self.trUtf8("<b>Espacios en blanco y comentarios:</b>")), 5, 0)
        grid.addWidget(QLabel(
            self.tr("{0}").format(len(self.get_comment_spaces(editor)))), 5, 1)
        grid.addWidget(QLabel(self.trUtf8("<b>Total de líneas:</b>")), 6, 0)
        grid.addWidget(QLabel(str(editor.lineas)), 6, 1)
        grid.addWidget(QLabel(self.trUtf8("<b>Modificado:</b>")), 7, 0)
        grid.addWidget(QLabel(self.tr(self.get_modification(filename))), 7, 1)

        btn_aceptar = QPushButton(self.tr("Aceptar"))
        grid.addWidget(btn_aceptar, 8, 1, Qt.AlignRight)

        vLayout.addLayout(grid)

        btn_aceptar.clicked.connect(self.close)

    def get_type(self, filename):
        try:
            ext = filename.split('.')[-1]
            if ext == 'c':
                type_ = self.trUtf8("Archivo fuente C")
            elif ext == 'h':
                type_ = self.trUtf8("Archivo cabecera")
            elif ext == 's':
                type_ = self.trUtf8("Código asm")
            return type_
        except:
            return filename.split('.')[-1].upper()

    def get_size(self, filename):
        size = (float(QFile(filename).size() + 1023.0) / 1024.0)
        return str(size)

    def get_comment_spaces(self, editor):
        spaces = re.findall('(^\n)|(^(\s+)?//)|(^( +)?($|\n))',
                            editor.texto, re.M)
        return spaces

    def get_modification(self, filename):
        try:
            time = os.path.getmtime(filename)
            format_time = datetime.fromtimestamp(
                time).strftime("%Y-%m-%d %H:%M")
            return format_time
        except:
            return "-"