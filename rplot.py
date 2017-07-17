"""
rplot.py is a stand-alone Python program which makes 
two-dimensional plots easier. 
It allows the user to create a map with colorbar and
a contour within one line of program.

You have to load mymap module from this file into your python program 
and use it as shown  in the following examples.

It works both for Python 2.7 and Python 3.x
--------------------------------------------------------------------------------------
A short description of variables:

maps : the main 2D object to be displayed
lo,lu: lower and upper limits to clip the map. if zero, full range will be used. 
extent: size of the map (two numbers for min/max in each axis), e.g. (0, 1., 0, 2.)

xt, yt, tit : position (in plot coordinate) and text of the title
xtt, ytt, mtn: a second annotation text

col: any python color table (gray, jet, ...)


fname: filename with extension, e.g. map.eps, file.jpg, ...
psave: path to save the figure
lev  : level for masks
mask : mask (a 2D map with the same size)
chk: flag. put it to zero to skip contours, or one to activate contours.
--------------------------------------------------------------------------------------
examples:

import matplotlib, numpy, rplot
from rplot import mymap
from pylab import cm

mu = 0.
std = 1.
n = 500
m = 2*n + 1
noise = numpy.random.normal(mu, std, (m,m)) * 0.2

#construct a 2D Gaussian
x, y = numpy.mgrid[-n:n+1, -n:n+1]
g = numpy.exp(-(x**2/float(n)+y**2/float(n))/100.) * 2.
gn = g + noise
extent=(0, g.shape[1], 0, g.shape[0])


example #1, simple 2D map with colorbar
mymap(g, 0.0, 0.0, extent, extent[1]*0.25, extent[3]*1.05,'noise', ' ',0., 0., 'gray', 100, './', 'test.jpg', 0, [1,2], g)


example #2, add title and annotation
mymap(g, 0.0, 0.0, extent, extent[1]*0.25, extent[3]*1.05,'title ','annotation', 200,400, 'gray', 100, './', 'test.jpg', 0, [1,2], g)


example #3, use color
mymap(g, 0.0, 0.0, extent, extent[1]*0.25, extent[3]*1.05,'title ','annotation', 200,400, 'jet', 100, './', 'test.jpg', 0, [1,2], g)


example #4, map with contour
mymap(gn, 0.0, 0.0, extent, extent[1]*0., extent[3]*1.05,'contour from original data','', 0,0, 'gray', 300,'./', 'test.jpg', 1, [0.5, 1.7], g)


example #5, map in a certain range of values + contour
mymap(gn, 0.0, 0.8, extent, extent[1]*0.15, extent[3]*1.05,'limited range','', 0,0, 'gray', 300,'./', 'test.jpg', 1, [0.1, 0.6], g)


example #6, map in color and contour gray
mymap(g, 0.0, 0.0, extent, extent[1]*(-0.05), extent[3]*1.05,'map in color and contour gray','',0.,0.,'jet', 300, './', 'test.jpg', 1, [.1, .3, .8], g)


example #7, map in gray and contour in color
mymap(g, 0.0, 0.0, extent, extent[1]*(-0.05), extent[3]*1.05,'map in gray and contour in color','',0.,0.,'gray', 300, './', 'test.jpg', 1, [.1, .3, .8], g)


This program is presented under MIT License. 

Copyright (c) Reza Rezaei

e-mail: reza5pm@gmail.com
"""

import pylab as plt
from pylab import *
import matplotlib, numpy
from matplotlib import verbose, ticker, patches
from matplotlib.patches import Ellipse, Circle, Arc, Arrow, Rectangle, Polygon, RegularPolygon
from mpl_toolkits.axes_grid1 import make_axes_locatable
import subprocess
mapf = 20
cbrf = 16

rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'
rcParams['xtick.major.size'] = 10
rcParams['xtick.minor.size'] = 5
rcParams['ytick.major.size'] = 8
rcParams['ytick.minor.size'] = 4
rcParams['xtick.major.pad'] = 8
rcParams['ytick.major.pad'] = 8
rcParams['xtick.labelsize'] = mapf
rcParams['ytick.labelsize'] = mapf
rcParams['axes.linewidth'] = 1 
rcParams['axes.labelcolor'] = 'black'
rcParams['verbose.level']= 'debug'
rcParams['font.size']= 2


def mymap(data, lo, lu, exten, xt, yt, tit, mtn, xtt, ytt, col, dpi, psave, fname, chk, lev, mask):
        if (lo == 0.)and(lu == 0.):
            lo = numpy.min(data)
            lu = numpy.min(data)
        else:
            data[where(data < lo)] = lo
            data[where(data > lu)] = lu
        if (xtt == 0.)and(ytt == 0.):
            xtt = 'arcsec'
            ytt = 'arcsec'
        else:
            xtt = 'Mm'
            ytt = 'Mm'
        resol = dpi
        fig = plt.figure()
        ax = fig.add_subplot(111)
        dc = '0.01'        
        im = imshow(data,origin='lower',interpolation='nearest',cmap=get_cmap(col),extent=exten,aspect=1)
        smax = exten[1]
        if (smax < 10.):
                ax.xaxis.set_minor_locator(MultipleLocator(1))
                ax.xaxis.set_major_locator(MultipleLocator(5))
        if (smax > 10.)and(smax <= 50.):
                ax.xaxis.set_minor_locator(MultipleLocator(5))
                ax.xaxis.set_major_locator(MultipleLocator(10))
        if (smax > 50.)and(smax <= 200.):
                ax.xaxis.set_minor_locator(MultipleLocator(10))
                ax.xaxis.set_major_locator(MultipleLocator(50))
        if (smax > 200.)and(smax < 1000.):
                ax.xaxis.set_minor_locator(MultipleLocator(100))
                ax.xaxis.set_major_locator(MultipleLocator(200))
        smax = exten[3]
        if (smax < 10.):
                ax.yaxis.set_minor_locator(MultipleLocator(1))
                ax.yaxis.set_major_locator(MultipleLocator(5))
        if (smax > 10.)and(smax <= 50.):
                ax.yaxis.set_minor_locator(MultipleLocator(5))
                ax.yaxis.set_major_locator(MultipleLocator(10))
        if (smax > 50.)and(smax <= 200.):
                ax.yaxis.set_minor_locator(MultipleLocator(10))
                ax.yaxis.set_major_locator(MultipleLocator(50))
        if (smax > 200.)and(smax < 1000.):
                ax.yaxis.set_minor_locator(MultipleLocator(100))
                ax.yaxis.set_major_locator(MultipleLocator(200))

        # add text for annotation        
        text(xt, yt, tit, fontsize=mapf-2, fontstyle='normal', family='sans-serif')
        text(0.1, 0.1, mtn, color='k', fontsize=mapf+2, bbox={'facecolor':'white', 'alpha':0.5, 'pad':10}, transform=ax.transAxes, family='sans-serif')
        
        for line in ax.get_xticklines() + ax.get_yticklines():
                line.set_markersize(10)
        ax.xaxis.set_tick_params(width=1.5)
        ax.yaxis.set_tick_params(width=1.5)
        rcParams['xtick.labelsize'] = cbrf
        rcParams['ytick.labelsize'] = cbrf
        xlabel(xtt, fontsize=mapf-2)
        ylabel(ytt, fontsize=mapf-2)

        # draw contours. for each contour set, we draw two curves.
        # the program select contours colors based on the map color table: color for b/w and b/w for color.
        rt = 1.
        if (len(lev) == 1):
                lev = [lev, lev]        
        if (chk > 0.)and(col == 'gray'):
                cset = contour(mask,lev,origin='lower',colors=['blue','red'],linewidths=(rt-0.5,rt-0.5),extent=exten)
                for c in cset.collections:
                        c.set_linestyle('solid')
                # activate to have a dashed two-colro contour        
                cset = contour(mask, lev, origin='lower',colors=['k','k'],linewidths=(rt-0.5,rt-0.5),extent=exten)
                for c in cset.collections:
                        c.set_linestyle('dashed')
                grid(which='minor', color='white', lw=1, alpha=0.2)

        if (chk > 0.)and(col != 'gray'):
                cset = contour(mask, lev, origin='lower',colors=['k', 'k'],linewidths=(rt-0.5,rt-0.5),extent=exten)
                for c in cset.collections:
                        c.set_linestyle('solid')
                # activate to have a dashed two-colro contour        
                cset = contour(mask, lev, origin='lower',colors=['0.6','white'],linewidths=(rt-0.5,rt-0.5),extent=exten)
                for c in cset.collections:
                        c.set_linestyle('dashed')
                grid(which='minor', color='black', lw=1, alpha=0.2)


        subplots_adjust(top=0.9, bottom=0.15,left=0.15, right=0.9, wspace=0.5, hspace=0.5)
        #ax.arrow(30, 140, -22., 3., lw=2, head_width=1.5, head_length=3., fc='cyan', ec='cyan'); text(12, 144, 'DC', fontsize=18, color='cyan')

        #colorbar(orientation='horizontal')#, ticks=(0, 45, 90, 135, 180), shrink=1.)
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.1)

        large = numpy.max(abs(data))
        if (large > 10.):
                digits = '%.0f'
        elif (large > 2.)and(large <= 10.):
                 digits = '%.1f'
        elif (large > 1.)and(large <= 2.):
                 digits = '%.2f'
        elif (large > 0.)and(large <= 1.):
                 digits = '%.3f'
        
        cb = colorbar(im, orientation='vertical', format=digits, cax=cax)
        tick_locator = ticker.MaxNLocator(nbins=5)
        cb.locator = tick_locator
        cb.update_ticks()

        
        file_out = psave+fname
        print(file_out)
        savefig(file_out, dpi=resol)#, boundingbox='tight')
        show()
        return 0

