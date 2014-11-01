# -*- coding: utf-8 -*-

# Copyright (C) <2014>  <Gabriel Acosta>
# This file is part of EDIS.

# EDIS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# EDIS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with EDIS.  If not, see <http://www.gnu.org/licenses/>.

from subprocess import Popen
from subprocess import PIPE


def comprobar():
    """ Devuelve una lista con las terminales disponibles en el sistema. """

    terminales = [
        "gnome-terminal",
        "x-terminal-emulator",
        "terminator",
        "guake",
        "lxterminal",
        "yakuake",
        "eterm",
        "rxvt",
        "wterm",
        "konsole",
        "xterm"
        ]

    ex = {}
    instaladas = []
    terminales = [terminales] if isinstance(terminales, str) else terminales
    for terminal in terminales:
        try:
            Popen([terminal, '--help'], stdout=PIPE, stderr=PIPE)
            ex[terminal] = True
        except OSError:
            ex[terminal] = False
    [instaladas.append(terminal) for terminal in terminales
        if ex[terminal]]

    return instaladas