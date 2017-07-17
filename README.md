rplot.py is a stand-alone Python program which makes 
two-dimensional plots easier. 
It allows the user to create a map with colorbar and
a contour within one line of program.

You have to load mymap module from this file into your python program 
and use it as shown  in the following examples.

It works both for Python 2.7 and Python 3.x
--------------------------------------------
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
------------------------------------------------------------------------

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