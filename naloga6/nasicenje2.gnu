#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex"    #3 grafi za vsak plot posebej


#set key box width 2 height 0.1 Left reverse invert samplen 1
#set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename1 = 'obrat1.txt'
filename2 = 'farmakoloski.dat'

n = 0.00955264
k = 0.20241427
y0 = 104.68307341
a = 21.18934798

f(x) = k*x + n

set xlabel '$t$'
set logscale y

set xrange [-0.025:1.025]
set yrange [:11000]
unset key

plot filename1 u 1:2 w lp lc -1 lt 7 notitle '$z$',\
f(x) lc 6 lw 2 notitle 

unset logscale y

set xlabel '$x$'
set format y ''
set format y2 '$%g$'
set y2tics 20

g(x) = y0*x/(x+a)

set xrange [-10:1010]
set yrange [-2:102]
set y2range [-2:102]
plot filename2 w lp lc -1 lt 7 notitle,\
g(x) lc 6 lw 2 notitle


unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
