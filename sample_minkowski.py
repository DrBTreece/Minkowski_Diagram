#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This sample does not actually report time in terms of ct (light-year)
# Modifications should be made

from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0,3,1000)
x = np.sin(2*np.pi*t)

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x,t)
ax.set_xlabel('1D position of Earth relative to Sun\n(units: Earth-Sun Distance)')
ax.set_ylabel('time (yrs)')
ax.set_aspect(3)
fig.tight_layout()
fig.show()
