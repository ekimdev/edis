# -*- coding: utf-8 -*-
# EDIS - a simple cross-platform IDE for C
#
# This file is part of EDIS
# Copyright 2014-2015 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)


from PyQt4.QtCore import QObject

from src.ui.menu import acciones
from src.ui.main import EDIS


class Menu(QObject):

    def __init__(self):
        QObject.__init__(self)
        # QActions
        self.acciones = list()

        for accion in acciones.ACCIONES:
            nombre = accion.get("nombre")
            conexion = accion.get("conexion")
            atajo = accion.get("atajo", None)
            icono = accion.get("icono", None)
            seccion = accion.get("seccion")
            separador = accion.get("separador", False)
            submenu = accion.get("submenu", False)
            qaccion = Accion(nombre, conexion, seccion, icono, atajo)
            qaccion.separador = separador
            qaccion.submenu = submenu
            self.acciones.append(qaccion)

        EDIS.cargar_componente("menu", self)


class Accion(object):

    """ Esta clase representa a una acción (QAction) """

    def __init__(self, nombre, conexion, seccion, icono=None, atajo=None):
        self.nombre = nombre
        self.conexion = conexion
        self.seccion = seccion
        self.icono = icono
        self.atajo = atajo
        self.separador = False
        self.submenu = False

menu = Menu()