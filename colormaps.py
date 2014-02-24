#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from __future__ import division
import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm
from matplotlib.pyplot import plot, scatter, boxplot, semilogx, semilogy, loglog, show, title, legend, figure, ylim, xlim, bar, imshow, savefig, subplot, get_cmap
import numpy as np


startcolor = '1'
n__ = 512
ga = 1.0

endcolor = '#FF0000'
cmap0 = col.LinearSegmentedColormap.from_list('0', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap0)


endcolor = '#FF4B00'
cmap1 = col.LinearSegmentedColormap.from_list('1', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap1)


endcolor = '#FF9600'
cmap2 = col.LinearSegmentedColormap.from_list('2', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap2)


endcolor = '#FFE100'
cmap3 = col.LinearSegmentedColormap.from_list('3', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap3)


endcolor = '#E1FF00'
cmap4 = col.LinearSegmentedColormap.from_list('4', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap4)


endcolor = '#96FF00'
cmap5 = col.LinearSegmentedColormap.from_list('5', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap5)

endcolor = '#4BFF00'
cmap6 = col.LinearSegmentedColormap.from_list('6', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap6)

endcolor = '#00FF00'
cmap7 = col.LinearSegmentedColormap.from_list('7', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap7)

endcolor = '#00FF4B'
cmap8 = col.LinearSegmentedColormap.from_list('8', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap8)

endcolor = '#00FF96'
cmap9 = col.LinearSegmentedColormap.from_list('9', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap9)


endcolor = '#00FFE1'
cmap10 = col.LinearSegmentedColormap.from_list('10', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap10)


endcolor = '#00E1FF'
cmap11 = col.LinearSegmentedColormap.from_list('11', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap11)


endcolor = '#0096FF'
cmap12 = col.LinearSegmentedColormap.from_list('12', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap12)


endcolor = '#004BFF'
cmap13 = col.LinearSegmentedColormap.from_list('13', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap13)

endcolor = '#0000FF'
cmap14 = col.LinearSegmentedColormap.from_list('14', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap14)

endcolor = '#4B00FF'
cmap15 = col.LinearSegmentedColormap.from_list('15', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap15)

endcolor = '#9600FF'
cmap16 = col.LinearSegmentedColormap.from_list('16', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap16)

endcolor = '#E100FF'
cmap17 = col.LinearSegmentedColormap.from_list('17', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap17)

endcolor = '#FF00E1'
cmap18 = col.LinearSegmentedColormap.from_list('18', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap18)

endcolor = '#FF0096'
cmap19 = col.LinearSegmentedColormap.from_list('19', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap19)





def show_cmaps(names):
    matplotlib.rc('text', usetex=False)
    a=np.outer(np.arange(0,1,0.01),np.ones(10))   # pseudo image data
    f=figure(figsize=(10,5))
    f.subplots_adjust(top=0.8,bottom=0.05,left=0.01,right=0.99)
    # get list of all colormap names
    # this only obtains names of built-in colormaps:
    maps=[m for m in cm.datad if not m.endswith("_r")]
    # use undocumented cmap_d dictionary instead
    maps = [m for m in cm.cmap_d if not m.endswith("_r")]
    maps.sort()
    # determine number of subplots to make
    l=len(maps)+1
    if names is not None: l=len(names)  # assume all names are correct!
    # loop over maps and plot the selected ones
    i=0
    for m in maps:
        if names is None or m in names:
            i+=1
            ax = subplot(1,l,i)
            ax.axis("off")
            imshow(a,aspect='auto',cmap=cm.get_cmap(m),origin="lower")
            title(m,rotation=90,fontsize=10,verticalalignment='bottom')
#    savefig("colormaps.png",dpi=100,facecolor='gray')
    show()

#names = [(str(n)) for n in range(20)]

#show_cmaps(names)


