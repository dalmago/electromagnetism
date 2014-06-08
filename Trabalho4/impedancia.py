#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#"THE BEER-WARE LICENSE" (Revision 42):
#
#<matheusdalmago10@hotmail.com> wrote this file. As long as you retain this
#notice you can do whatever you want with this stuff. If we meet some day,
#and you think this stuff is worth it, you can buy me a beer in return.
#
#Created: 2014-06-08
#       by: Matheus Dal Mago
#

"""
    Calcular Z0 para diversos valores de R', C', G', L' e f.
"""

import numpy as np

print ('Digite os valores solicitados:')

f = float(input('Frequência [Hz]: '))
R = float(input('Resistência série R\' [Ω/m]: '))
L = float(input('Indutância série L\' [H/m]: '))
G = float(input('Condutância paralelo G\' [S/m]: '))
C = float(input('Capacitância paralelo C\' [F/m]: '))

omega = 2*np.pi*f

Z = complex(R, omega*L)
Y = complex(G, omega*C)

Z0 = np.sqrt(Z/Y)

print ('\n\nImpedância característica Z0 = ' + str(Z0) + ' [Ω]')
