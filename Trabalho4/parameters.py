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
#Created: 2014-06-07
#       by: Matheus Dal Mago
#

"""
    Fazer um simulador para calcular R', G', L' e C' das linhas de
    transmissão, fornecendo as dimensões e as propriedades dos materiais
    σc, µ, εr, σd.
"""

try:
    import numpy as np
except ImportError:
    print("É preciso instalar a biblioteca numpy")

print('Digite os parametros abaixo:')

#muR = float(input('Permeabilidade relativa do condutor: '))
mu0 = 4*np.pi*10**(-7)
sigmaC = float(input('Condutividade do condutor (σc)[S/m]: '))
sigmaD = float(input('Condutividade do dielétrico (σd)[S/m]: '))
epsilonR = float(input('Permissividade dielétrica relativa (εr)[F/m]: '))
epsilon0 = 8.854*10**(-12)
f = float(input('Frequência do sinal [Hz]: '))

if int(input('Digite 1 para cabo coaxial e 2 para paralelo: ')) == 1:
    a=float(input('Raio interno do cabo [mm]: '))
    b=float(input('Raio externo do cabo [mm]: '))

    R = (1000/(2*np.pi))*(1/a + 1/b)*np.sqrt(np.pi*f*mu0/sigmaC)
    L = mu0*np.log(b/a)/(2*np.pi)
    G = 2*np.pi*sigmaD/np.log(b/a)
    C = 2*np.pi*epsilon0*epsilonR/np.log(b/a)

else:
    a = float(input('Raio do condutor [mm]: '))
    d = float(input('Distância entre os condutores [mm]: '))

    R = (1000/a)*np.sqrt(f*mu0/sigmaC)
    L = (mu0/np.pi)*np.arccosh(d/(2*a))
    G = np.pi*sigmaD/np.arccosh(d/(2*a))
    C = np.pi*epsilon0*epsilonR/np.arccosh(d/(2*a))

print ('\n\nResistência do condutor (R\') [Ω/m] = %f' % R)
print ('Indutância série (L\') [H/m] = %f' % L)
print ('Condutância do dielétrico (G\') [S/m] = %f' % G)
print ('Capacitância (C\') [F/m] = %f' % C)
