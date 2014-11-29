# -*- coding: utf-8 -*-
# EDIS - Entorno de Desarrollo Integrado Simple para C/C++
#
# This file is part of EDIS
# Copyright 2014 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

# Módulos Python
import os

from PyQt4.QtGui import (
    QSizePolicy
    )

# Módulos QtCore
from PyQt4.QtCore import QObject
#from PyQt4.QtCore import SIGNAL

# Módulos EDIS
from src import recursos
from src.helpers import configuraciones
from src.ui.widgets.creador_widget import (
    crear_accion,
    create_button
    )

_TUX = configuraciones.LINUX
_ICONO = recursos.ICONOS
_ATAJO = recursos.ATAJOS


class MenuEjecucion(QObject):

    def __init__(self, menu_codigo, toolbar, ide):
        super(MenuEjecucion, self).__init__()

        self.ide = ide

        # Acciones #
        # Compilar
        self.accionCompilar = crear_accion(self, "Compilar",
            icono=_ICONO['build'],
            slot=self.ide.distribuidor.compilar)
        # Ejecutar
        self.accionEjecutar = crear_accion(self, "Ejecutar",
            icono=_ICONO['run'], slot=self.ide.distribuidor.ejecutar)

        # Agregar acciones al menú #
        menu_codigo.addAction(self.accionCompilar)
        menu_codigo.addAction(self.accionEjecutar)

        self.tool_compilar = create_button(self.ide, text=self.tr("Compilar"),
            shortcut=_ATAJO['compilar'], action=self.accionCompilar)
        self.tool_compilar.setSizePolicy(QSizePolicy.MinimumExpanding,
            QSizePolicy.Maximum)

        self.tool_ejecutar = create_button(self.ide, text=self.tr("Ejecutar"),
            shortcut=_ATAJO['ejecutar'], action=self.accionEjecutar)
        self.tool_ejecutar.setSizePolicy(QSizePolicy.MinimumExpanding,
            QSizePolicy.Maximum)

        self.items_toolbar = {
            "compilar-archivo": self.tool_compilar,
            "ejecutar-archivo": self.tool_ejecutar
            }

    def metodo_ejecutar(self):
        self.ide.contenedor_secundario.ejecutar_archivo(self.comp)

    def metodo_compilar_ejecutar(self):
        editorW = self.ide.contenedor_principal.devolver_editor_actual()
        if not editorW:
            return None

        path_name = self.ide.contenedor_principal.guardar_archivo(editorW)
        if not path_name:
            return None
        salida = os.path.basename(path_name).split('.')[0]
        self.ide.contenedor_secundario.compilar_archivo(salida, path_name)
        self.ide.contenedor_secundario.ejecutar_archivo(self.comp)