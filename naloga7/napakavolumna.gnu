#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf3b.tex"    #Tukaj gledam napako zaradi razlicnega stevila vzorcev

set key box width 1 height 0.1 Left reverse invert samplen 1
#set key title 'volumen'
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

#set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP


set samples 10000
filename = 'telo/napaka_volumna.txt'

set logscale x
set format x '$10^{%L}$'
set xtics add ('$1$' 1, '$10$' 10)

set xrange [0.9:1500000]
#set yrange [0:]

#plot filename u 3:1 w lp ps .5 lt 7 lc 6 lw 2 title '$V$'


set format y ''
set format y2 '$%g$'
set y2tics 0.02
set y2range [0:]

f(x) = a/(sqrt(x+b))
a = 1
fit f(x) filename u 3:2 via a,b#,c

plot filename u 3:2 axes x1y2 w lp ps .6 lt 7 lc 6 lw 3 title '$\sigma_{V}$',\
f(x) axes x1y2 lc -1 lw 1.5 dt 2 title '$f(x) = 1/\sqrt{x}$'

#unset multiplot

#unset term
#set term dumb
#unset out
#set out '/dev/null'
