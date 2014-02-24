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

endcolor = '#A6CEE3'
cmap0 = col.LinearSegmentedColormap.from_list('0', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap0)

endcolor = '#1F78B4'
cmap1 = col.LinearSegmentedColormap.from_list('1', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap1)

endcolor = '#B2DF8A'
cmap2 = col.LinearSegmentedColormap.from_list('2', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap2)

endcolor = '#33A02C'
cmap3 = col.LinearSegmentedColormap.from_list('3', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap3)

endcolor = '#FB9A99'
cmap4 = col.LinearSegmentedColormap.from_list('4', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap4)

endcolor = '#E31A1C'
cmap5 = col.LinearSegmentedColormap.from_list('5', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap5)

endcolor = '#FDBF6F'
cmap6 = col.LinearSegmentedColormap.from_list('6', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap6)

endcolor = '#FF7F00'
cmap7 = col.LinearSegmentedColormap.from_list('7', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap7)

endcolor = '#CAB2D6'
cmap8 = col.LinearSegmentedColormap.from_list('8', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap8)

endcolor = '#6A3D9A'
cmap9 = col.LinearSegmentedColormap.from_list('9', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap9)

endcolor = '#FFFF99'
cmap10 = col.LinearSegmentedColormap.from_list('10', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap10)

endcolor = '#B15928'
cmap11 = col.LinearSegmentedColormap.from_list('11', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap11)

endcolor = '#A6CEE3'
cmap12 = col.LinearSegmentedColormap.from_list('12', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap12)

endcolor = '#1F78B4'
cmap13 = col.LinearSegmentedColormap.from_list('13', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap13)

endcolor = '#B2DF8A'
cmap14 = col.LinearSegmentedColormap.from_list('14', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap14)

endcolor = '#33A02C'
cmap15 = col.LinearSegmentedColormap.from_list('15', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap15)

endcolor = '#FB9A99'
cmap16 = col.LinearSegmentedColormap.from_list('16', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap16)

endcolor = '#E31A1C'
cmap17 = col.LinearSegmentedColormap.from_list('17', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap17)

endcolor = '#FDBF6F'
cmap18 = col.LinearSegmentedColormap.from_list('18', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap18)

endcolor = '#FF7F00'
cmap19 = col.LinearSegmentedColormap.from_list('19', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap19)

endcolor = '#CAB2D6'
cmap20 = col.LinearSegmentedColormap.from_list('20', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap20)

endcolor = '#6A3D9A'
cmap21 = col.LinearSegmentedColormap.from_list('21', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap21)

endcolor = '#FFFF99'
cmap22 = col.LinearSegmentedColormap.from_list('22', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap22)

endcolor = '#B15928'
cmap23 = col.LinearSegmentedColormap.from_list('23', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap23)

endcolor = '#FFFF99'
cmap24 = col.LinearSegmentedColormap.from_list('24', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap24)

endcolor = '#B15928'
cmap25 = col.LinearSegmentedColormap.from_list('25', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap25)

endcolor = '#A6CEE3'
cmap26 = col.LinearSegmentedColormap.from_list('26', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap26)

endcolor = '#1F78B4'
cmap27 = col.LinearSegmentedColormap.from_list('27', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap27)

endcolor = '#B2DF8A'
cmap28 = col.LinearSegmentedColormap.from_list('28', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap28)

endcolor = '#33A02C'
cmap29 = col.LinearSegmentedColormap.from_list('29', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap29)

endcolor = '#FB9A99'
cmap30 = col.LinearSegmentedColormap.from_list('30', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap30)

endcolor = '#E31A1C'
cmap31 = col.LinearSegmentedColormap.from_list('31', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap31)

endcolor = '#FDBF6F'
cmap32 = col.LinearSegmentedColormap.from_list('32', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap32)

endcolor = '#FF7F00'
cmap33 = col.LinearSegmentedColormap.from_list('33', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap33)

endcolor = '#CAB2D6'
cmap34 = col.LinearSegmentedColormap.from_list('34', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap34)

endcolor = '#6A3D9A'
cmap35 = col.LinearSegmentedColormap.from_list('35', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap35)

endcolor = '#FFFF99'
cmap36 = col.LinearSegmentedColormap.from_list('36', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap36)

endcolor = '#B15928'
cmap37 = col.LinearSegmentedColormap.from_list('37', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap37)

endcolor = '#A6CEE3'
cmap38 = col.LinearSegmentedColormap.from_list('38', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap38)

endcolor = '#1F78B4'
cmap39 = col.LinearSegmentedColormap.from_list('39', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap39)

endcolor = '#B2DF8A'
cmap40 = col.LinearSegmentedColormap.from_list('40', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap40)

endcolor = '#33A02C'
cmap41 = col.LinearSegmentedColormap.from_list('41', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap41)

endcolor = '#FB9A99'
cmap42 = col.LinearSegmentedColormap.from_list('42', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap42)

endcolor = '#E31A1C'
cmap43 = col.LinearSegmentedColormap.from_list('43', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap43)

endcolor = '#FDBF6F'
cmap44 = col.LinearSegmentedColormap.from_list('44', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap44)

endcolor = '#FF7F00'
cmap45 = col.LinearSegmentedColormap.from_list('45', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap45)

endcolor = '#CAB2D6'
cmap46 = col.LinearSegmentedColormap.from_list('46', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap46)

endcolor = '#6A3D9A'
cmap47 = col.LinearSegmentedColormap.from_list('47', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap47)

endcolor = '#FFFF99'
cmap48 = col.LinearSegmentedColormap.from_list('48', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap48)

endcolor = '#B15928'
cmap49 = col.LinearSegmentedColormap.from_list('49', [startcolor,endcolor], N = n__, gamma=ga)
cm.register_cmap(cmap=cmap49)





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
    show()

#names = [(str(n)) for n in range(50)]
#show_cmaps(names)


