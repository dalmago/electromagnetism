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
#Created: 2014-03-26
#       by: Matheus Dal Mago
#

import numpy as np

class Runner(object):
        def __init__(self):
                self.input()

        def input(self):
                self.x1 = int(input("Digite a coordenada X da carga Q: "))
                self.y1 = int(input("Digite a coordenada Y da carga Q: "))
                self.z1 = int(input("Digite a coordenada Z da carga Q: "))

                self.carga = float(input("Digita o valor da carga Q (C): "))

                self.x = int(input("Digite a coordenada X do ponto P: "))
                self.y = int(input("Digite a coordenada Y do ponto P: "))
                self.z = int(input("Digite a coordenada Z do ponto P: "))

        def run(self):
                self.calcula()
                self.output()

        def calcula(self):
                self.vector = [self.x1-self.x, self.y1-self.y,\
                        self.z1-self.z]

                self.modulo = np.sqrt((self.vector[0]**2)+\
                        (self.vector[1]**2)+\
                        (self.vector[2]**2))

                self.unitario = np.array([\
                        float(self.vector[0]/self.modulo),\
                        float(self.vector[1]/self.modulo),\
                        float(self.vector[2]/self.modulo)])

                self.valor = ((9*10**9)*self.carga)/self.modulo**2

                self.componentes = self.valor*self.unitario

        def output(self):
                print ("modulo da distancia entre Q e P")
                print (self.modulo)

                print ("vetor unitário")
                print (self.unitario)

                print ("Componentes Ex, Ey, Ez do campo elétrico no ponto P, originado pela carga Q, em N/C")
                print (self.componentes)

if __name__ == "__main__":
        runner = Runner()
        runner.run()
