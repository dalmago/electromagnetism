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
    Fazer simulaçẽos para cálculo de γ, λ, α, β, velocidade...
"""

import numpy as np

print ('Digite os valores solicitados:')

f = float(input('Frequência [Hz]: '))
R = float(input('Resistência série R\' [Ω/m]: '))
L = float(input('Indutância série L\' [H/m]: '))
G = float(input('Condutância paralelo G\' [S/m]: '))
C = float(input('Capacitância paralelo C\' [F/m]: '))

omega = 2*np.pi*f

gama = np.sqrt(complex(R, omega*L)*complex(G, omega*C))

alfa = gama.real
beta = gama.imag

v = omega/beta
fracao = v/(3*10**8)
lamda = 2*np.pi/beta

Z = complex(R, omega*L)
Y = complex(G, omega*C)

print ('\n\nComponente α = ' + str(alfa) + ' [neper/m]')
print ('Componente β = ' + str(beta) + ' [rad/m]')
print ('Constante de progapação γ = ' + str(gama) + '[1/m]')
print ('Comprimento de onda λ = ' + str(lamda) + ' [m]')
print ('Velocidade de propagação = ' + str(v) + ' [m/s]')
print ('Fração da velocidade da luz: ' + str(fracao))
print ('Impedância Z\' = ' + str(Z) + ' [Ω/m]')
print ('Admitância Y\' = ' + str(Y) + ' [S/m]')

print ('\n V=V0.e^(-{alfa}z).cos({omega}t-{beta}z+phi)'.format(alfa=str(alfa),\
        omega=str(omega), beta=str(beta)))
