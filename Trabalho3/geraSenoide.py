#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#Created: 2014-05-28
#       by: Matheus Dal Mago
#

import matplotlib.pyplot as plt
import numpy as np

w = 2*np.pi*60 # w=2*pi*f

x = np.arange(0, 0.1, 0.0001)

y = 5*np.sqrt(2)*np.cos(w*x)

plt.plot(x,y)

plt.xlim(0, 0.1)
plt.ylim(-10, 10)
plt.xlabel('t [s]')
plt.ylabel('Tensao [V]')
plt.axhline(color='black')

plt.show()
