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
#Created: 2014-05-28
#       by: Matheus Dal Mago
#
# Just draw some parts of a class experiment

import matplotlib.pyplot as plt
import numpy as np

plt.xlim(-0.05,9.05)
plt.ylim(-0.05,6.05)

plt.plot([5,5.8],[4.1,4.1],'k')
plt.plot([5,5.8],[4.9,4.9],'k')

plt.plot([5,5],[4.1,4.9],'k')
plt.plot([5.8,5.8],[4.1,4.9],'k')

plt.plot([5,5.8],[4.1,4.9], 'k')
plt.plot([5,5.8],[4.9,4.1], 'k')

plt.xlabel('cm')
plt.ylabel('cm')

plt.text(5, 3.7, 'condutor')

plt.plot([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5], np.zeros(shape=9), \
        'ob')
plt.plot([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5], [6,6,6,6,6,6,6,6,6],\
        'ob')

plt.plot(np.zeros(shape=6), [0.5, 1.5, 2.5, 3.5, 4.5, 5.5], 'ob')
plt.plot([9,9,9,9,9,9], [0.5, 1.5, 2.5, 3.5, 4.5, 5.5], 'ob')
plt.show()
