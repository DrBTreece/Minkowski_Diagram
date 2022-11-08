# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:37:38 2022

@author: btreece
"""

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

t = np.linspace(0,3,1000)
beta = 0.4
x_obs0 = 0*t
x_obs1 = beta*t


def plot_observer_trajectories(t, x_0, x_1):
    # Initialize Plots
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Offsets for text placement
    trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
                                       x=-0.3, y=0.0, units='inches')
    
    # Plot Light Cone
    ax.plot(-t, t, color = 'black', linewidth = 1)
    ax.plot(t,t, color = 'black', linewidth = 1)
    
    # Plot Observer Trajectories
    line0, = ax.plot(x_0,t, color = 'blue', linewidth = 3)
    line1, = ax.plot(x_1,t, color = 'red', linewidth = 3)
    
    # Text
      # Light Cone
    ax.text(1.2*t[len(t)//2], 0.8*t[len(t)//2], 'light-cone', rotation=45, transform=trans_offset)
    ax.text(-1.2*t[len(t)//2], 0.8*t[len(t)//2], 'light-cone', rotation=-45, transform=trans_offset)
      # Observers
    ax.text(x_0[-1], 1.03*t[-1], 'Observer 0', color = 'blue', transform=trans_offset)
    ax.text(x_1[-1], 1.03*t[-1], 'Observer 1', color = 'red', transform=trans_offset)
    
    # Plot Formatting
    ax.set_xlabel('x (light-yrs)')
    ax.set_ylabel('ct (light-yrs)')
    ax.set_xlim((-1.1*t[-1], 1.1*t[-1]))
    ax.set_ylim((-0.05*t[-1], 1.1*t[-1]))
    ax.set_aspect(1)
    fig.tight_layout()
    fig.show()
    
    return fig,ax,[line0, line1]
    
fig, ax, lines = plot_observer_trajectories(t, x_obs0, x_obs1)