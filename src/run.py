# -*- coding: utf-8 -*-
# EDIS - a simple cross-platform IDE for C
#
# This file is part of EDIS
# Copyright 2014-2015 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

import sys
import os

from PyQt4.QtGui import QIcon

from PyQt4.QtCore import (
    QLocale,
    QTranslator,
    QLibraryInfo
    )
from src import paths
from src.helpers.configuracion import ESettings

#lint:disable
from src.ui.widgets import barra_de_estado
import src.ui.contenedores.principal
import src.ui.contenedores.output.contenedor_secundario
import src.ui.contenedores.lateral.navegador
import src.ui.contenedores.lateral.explorador
import src.ui.contenedores.lateral.arbol_simbolos
import src.ui.menu.menu
#lint:enable
from src.ui.main import EDIS


def correr_interfaz(app):
    ESettings().cargar()
    import src.ui.inicio  # lint:ok
    # Traductor
    local = QLocale.system().name()
    qtraductor = QTranslator()
    qtraductor.load("qt_" + local, QLibraryInfo.location(
                    QLibraryInfo.TranslationsPath))

    edis = EDIS()
    app.setWindowIcon(QIcon(paths.ICONOS['icon']))
    # Aplicar estilo
    with open(os.path.join(paths.PATH,
              "extras", "temas", "default.qss")) as tema:
        estilo = tema.read()
    app.setStyleSheet(estilo)
    # Archivos de última sesión
    archivos = ESettings.get('general/archivos')
    # Archivos recientes
    recents_files = ESettings.get('general/recientes')
    if recents_files is None:
        recents_files = []
    edis.cargar_archivos(archivos, recents_files)
    edis.show()
    sys.exit(app.exec_())