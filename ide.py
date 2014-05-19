#-*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QDesktopWidget
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QToolBar
from PyQt4.QtGui import QApplication

from PyQt4.QtCore import Qt

from side_c.gui.menu import menu_archivo
from side_c.gui.menu import menu_editar
from side_c.gui.menu import menu_ver
from side_c.gui.menu import menu_codigo
from side_c.gui.menu import menu_acerca_de

from side_c.gui import widget_central

from side_c import recursos

ITEMS_TOOLBAR = [
    "nuevo-archivo",
    "abrir-archivo",
    "guardar-archivo",
    "guardar-como-archivo",
    "separador",
    "compilar-archivo",
    "ejecutar-archivo",
    "compilar_ejecutar-archivo",
    "separador"
    ]


class IDE(QMainWindow):
    """ Contenedor principal """

    def __init__(self):
        super(IDE, self).__init__()
        self.setMinimumSize(800, 600)
        self.setWindowTitle('SIDE-C - Version: 0.x DEV')
        self._cargar_tema()
        get_pantalla = QDesktopWidget().screenGeometry()
        self.posicionar_ventana(get_pantalla)
        self.setWindowIcon(QIcon(recursos.ICONOS['icono']))

        self.widget_Central = widget_central.WidgetCentral()
        self.setCentralWidget(self.widget_Central)

        # Barra de estado
        self.toolBar = self.statusBar()
        self.toolBar.showMessage("SIDE")

        # ToolBar
        self.toolbar = QToolBar(self)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.addToolBar(2, self.toolbar)

        # Menu
        menu = self.menuBar()
        archivo = menu.addMenu(self.tr("&Archivo"))
        editar = menu.addMenu(self.tr("&Editar"))
        ver = menu.addMenu(self.trUtf8("&Ver"))
        codigo = menu.addMenu(self.trUtf8("&Codigo fuente"))
        acerca = menu.addMenu(self.tr("Ace&rca de"))

        self._menu_archivo = menu_archivo.MenuArchivo(
            archivo, self.toolbar, self)
        self._menu_editar = menu_editar.MenuEditar(editar, self)
        self._menu_ver = menu_ver.MenuVer(ver, self)
        self._menu_codigo = menu_codigo.MenuCodigoFuente(
            codigo, self.toolbar, self)
        self._menu_acerca_de = menu_acerca_de.MenuAcercade(acerca, self)

        # Cargar items en la toolbar
        self.cargar_toolbar()

    def posicionar_ventana(self, pantalla):
        """ Posiciona la ventana en el centro de la pantalla. """

        tam_ventana = self.geometry()

        self.move((pantalla.width() - tam_ventana.width()) / 2,
                  (pantalla.height() - tam_ventana.height()) / 2)

    def cargar_toolbar(self):
        """ Carga los items en la toolbar """

        self.toolbar.clear()
        items_toolbar = {}
        items_toolbar.update(self._menu_archivo.items_toolbar)
        items_toolbar.update(self._menu_codigo.items_toolbar)

        for i in ITEMS_TOOLBAR:
            if i == "separador":
                self.toolbar.addSeparator()
            else:
                item_tool = items_toolbar.get(i, None)
                if item_tool is None:
                    pass
                else:
                    self.toolbar.addAction(item_tool)

    def _cargar_tema(self):
        qss = recursos.TEMA_POR_DEFECTO

        with open(qss) as q:
            tema = q.read()
        QApplication.instance().setStyleSheet(tema)