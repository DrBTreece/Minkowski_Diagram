# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:37:38 2022

@author: btreece
"""

from matplotlib import pyplot as plt
import numpy as np
import matplotlib.transforms as mtransforms

# def plot_observer_trajectories(t, x_0, x_1):
#     # Initialize Plots
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
    
#     # Offsets for text placement
#     trans_offset = mtransforms.offset_copy(ax.transData, fig=fig,
#                                        x=-0.3, y=0.0, units='inches')
    
#     # Plot Light Cone
#     ax.plot(-t, t, color = 'black', linewidth = 1)
#     ax.plot(t,t, color = 'black', linewidth = 1)
    
#     # Plot Observer Trajectories
#     line0, = ax.plot(x_0,t, color = 'blue', linewidth = 3)
#     line1, = ax.plot(x_1,t, color = 'red', linewidth = 3)
    
#     # Text
#       # Light Cone
#     ax.text(1.2*t[len(t)//2], 0.8*t[len(t)//2], 'light-cone', rotation=45, transform=trans_offset)
#     ax.text(-1.2*t[len(t)//2], 0.8*t[len(t)//2], 'light-cone', rotation=-45, transform=trans_offset)
#       # Observers
#     ax.text(x_0[-1], 1.03*t[-1], 'Observer 0', color = 'blue', transform=trans_offset)
#     ax.text(x_1[-1], 1.03*t[-1], 'Observer 1', color = 'red', transform=trans_offset)
    
#     # Plot Formatting
#     ax.set_xlabel('x (light-yrs)')
#     ax.set_ylabel('ct (light-yrs)')
#     ax.set_xlim((-1.1*t[-1], 1.1*t[-1]))
#     ax.set_ylim((-0.05*t[-1], 1.1*t[-1]))
#     ax.set_aspect(1)
#     fig.tight_layout()
#     fig.show()
    
#     return fig,ax,[line0, line1]
    
# fig, ax, lines = plot_observer_trajectories(t, x_obs0, x_obs1)

def add_to_plot(x, y, ax=None, **plt_kwargs):
    if ax is None:
        ax = plt.gca()
    ax.plot(x, y, **plt_kwargs)
    return (ax)

def format_plot(ax):
    ax.set_xlabel('x (light-yrs)')
    ax.set_ylabel('ct (light-yrs)')
    temp = ax.get_lines()
    xmin = np.min([np.min(i.get_xdata()) for i in temp])
    xmax = np.max([np.max(i.get_xdata()) for i in temp])
    ymin = np.min([np.min(i.get_ydata()) for i in temp])
    ymax = np.max([np.max(i.get_ydata()) for i in temp])

    ax.set_xlim((xmin - 0.05*(xmax-xmin), xmax + 0.05*(xmax-xmin)))
    ax.set_ylim((ymin - 0.05*(ymax-ymin), ymax + 0.05*(ymax-ymin)))
    ax.set_aspect(1)
    fig = ax.get_figure()
    fig.tight_layout()
    

def add_light_cones(x0, y0, ax, timeforward=True):

    # (xmin, xmax) = ax.get_xlim()
    # (ymin, ymax) = ax.get_ylim()
    temp = ax.get_lines()
    xmin = np.min([np.min(i.get_xdata()) for i in temp])
    xmax = np.max([np.max(i.get_xdata()) for i in temp])
    ymin = np.min([np.min(i.get_ydata()) for i in temp])
    ymax = np.max([np.max(i.get_ydata()) for i in temp])
    
    if timeforward:
        negdist = min(x0 - xmin, ymax - y0)
        posdist = min(xmax - x0, ymax - y0)
        ax.plot([x0 - negdist, x0], [y0 + negdist, y0], color='black', linewidth=1)
        ax.plot([x0, x0 + posdist], [y0, y0 + posdist], color='black', linewidth=1)
    else:
        negdist = min(x0 - xmin, y0 - ymin)
        posdist = min(xmax - x0, y0 - ymin)
        ax.plot([x0 - negdist, x0], [y0 - negdist, y0], color='black', linewidth=1)
        ax.plot([x0, x0 + posdist], [y0, y0 - posdist], color='black', linewidth=1)

def extract_position_at_time(time, t_array, x_array):
    indx = np.argwhere( np.abs(t_array - time) == np.min(np.abs(t_array - time)) )
    if t_array[indx] <= time:
        return x_array[indx] + (x_array[indx+1] - x_array[indx])*(time - t_array[indx])/(t_array[indx+1] - t_array[indx])
    else:
        return x_array[indx] - (x_array[indx] - x_array[indx-1])*(t_array[indx]-time)/(t_array[indx] - t_array[indx-1])

t = np.linspace(0,3,1000)

# Observer 0 has no speed
x_obs0 = 0*t
# Observer 1 has a speed equal to 0.8*c
x_obs1 = 0.8*t

lt = 1.15
lx0 = extract_position_at_time(lt, t, x_obs0)[0,0]
lx1 = extract_position_at_time(lt, t, x_obs1)[0,0]

ax = add_to_plot(x_obs0,t, color = 'blue', linewidth = 3)
add_to_plot(x_obs1,t, ax = ax, color = 'red', linewidth = 3)
add_to_plot(np.array([lx0, lx1]), np.array([lt, lt]), ax = ax, color = (0.0, 0.6, 0.6), linewidth = 2)
format_plot(ax)
add_light_cones(0,0,ax)    