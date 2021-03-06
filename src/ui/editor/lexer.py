# -*- coding: utf-8 -*-
# EDIS - a simple cross-platform IDE for C
#
# This file is part of EDIS
# Copyright 2014-2015 - Gabriel Acosta
# License: GPLv3 (see http://www.gnu.org/licenses/gpl.html)

from PyQt4.Qsci import QsciLexerCPP
from PyQt4.QtGui import QColor

from src import recursos


class LexerC(QsciLexerCPP):

    def __init__(self, *args, **kwargs):
        super(LexerC, self).__init__(*args, **kwargs)
        # Configuración
        self.setStylePreprocessor(True)
        self.setFoldComments(True)
        self.setFoldPreprocessor(True)

        self.__cargar_highlighter()

    def __cargar_highlighter(self):
        self.setDefaultPaper(QColor(recursos.TEMA['FondoEditor']))
        self.setPaper(self.defaultPaper(0))
        self.setColor(QColor(recursos.TEMA['Color']))

        tipos = dir(LexerC)
        for tipo in tipos:
            if tipo in recursos.TEMA:
                atr = getattr(self, tipo)
                self.setColor(QColor(recursos.TEMA[tipo]), atr)

    def keywords(self, clave):
        super(LexerC, self).keywords(clave)
        if clave == 1:
            return ('auto break case const continue default do else enum'
                    'extern for goto if return sizeof struct switch typedef'
                    'union while')
        elif clave == 2:
            return ('char double float int long register short signed static'
                    'unsigned void volatile')