# -*- coding: utf-8 -*-
# EDIS - a simple cross-platform IDE for C
#
# This file is part of EDIS
# Copyright 2014-2015 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

import sys

from PyQt4.QtCore import QSettings

from src import paths


LINUX = False
WINDOWS = False

#FIXME: Mac OS
if sys.platform == 'linux':
    LINUX = True
    FUENTE = 'Monospace'
    TERMINAL = ''
elif sys.platform == 'win32':
    WINDOWS = True
    FUENTE = 'Courier'

ITEMS_TOOLBAR = [
    'Nuevo archivo',
    'Abrir',
    'Guardar',
    'separador',
    'Deshacer',
    'separador',
    'Rehacer',
    'separador',
    'Indentar',
    'Remover indentación',
    'Compilar',
    'Ejecutar',
    'Terminar',
    'separador'
    ]

# Configuracion por defecto
# configuracion[clave_QSettings] = valor_QSettings
configuracion = {
    'ventana/dimensiones': 0,
    'ventana/posicion': 0,
    'ventana/guardarDimensiones': True,
    'general/confirmarSalida': True,
    'editor/margen': True,
    'editor/margenAncho': 80,
    'editor/tipoCursor': 2,  # 0: invisilbe; 1: línea; 2: bloque
    'editor/indentacion': True,
    'editor/indentacionAncho': 4,
    'editor/guias': False,
    'editor/mostrarTabs': False,
    'editor/modoWrap': False,
    'editor/fuente': "",
    'editor/fuenteTam': 10,
    'general/inicio': True,
    'general/archivos': [],
    'general/recientes': [],
    'terminal': ''
    }

#FIXME:
RECIENTES = []


class ESettings(object):

    def cargar(self):
        """ Carga las configuraciones desde el archivo .ini

        QSettings.value(clave, valor, type=tipo)
        """

        qconfig = QSettings(paths.CONFIGURACION, QSettings.IniFormat)
        configuracion['ventana/dimensiones'] = qconfig.value(
            'ventana/dimensiones', type='QSize')
        configuracion['ventana/posicion'] = qconfig.value(
            'ventana/posicion', type='QPoint')
        configuracion['general/inicio'] = qconfig.value(
            'general/inicio', True, type=bool)
        configuracion['ventana/guardarDimensiones'] = qconfig.value(
            'ventana/guardarDimensiones', True, type=bool)
        configuracion['general/confirmarSalida'] = qconfig.value(
            'general/confirmarSalida', True, type=bool)
        configuracion['editor/margen'] = qconfig.value(
            'editor/margen', True, type=bool)
        configuracion['editor/margenAncho'] = qconfig.value(
            'editor/margenAncho', 80, type=int)
        configuracion['editor/tipoCursor'] = qconfig.value(
            'editor/tipoCursor', 2, type=int)
        configuracion['editor/indentacion'] = qconfig.value(
            'editor/indentacion', True, type=bool)
        configuracion['editor/indentacionAncho'] = qconfig.value(
            'editor/indentacionAncho', 4, type=int)
        configuracion['editor/guias'] = qconfig.value(
            'editor/guias', False, type=bool)
        configuracion['editor/mostrarTabs'] = qconfig.value(
            'editor/mostrarTabs', False, type=bool)
        configuracion['editor/modoWrap'] = qconfig.value(
            'editor/modoWrap', False, type=bool)
        configuracion['editor/fuente'] = qconfig.value(
            'editor/fuente', "", type=str)
        configuracion['editor/fuenteTam'] = qconfig.value(
            'editor/fuenteTam', 11, type=int)
        configuracion['general/archivos'] = qconfig.value(
            'general/archivos', [])
        configuracion['general/recientes'] = qconfig.value(
            'general/recientes', [])

    @staticmethod
    def get(valor):
        return configuracion[valor]

    @staticmethod
    def set(clave, valor):
        qconfig = QSettings(paths.CONFIGURACION, QSettings.IniFormat)
        configuracion[clave] = valor
        qconfig.setValue(clave, valor)

    @staticmethod
    def borrar():
        QSettings(paths.CONFIGURACION, QSettings.IniFormat).clear()