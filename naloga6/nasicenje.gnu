#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"    #3 grafi za vsak plot posebej


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

f(x) = k*x + n
fit f(x) filename1 u 1:2 via k,n

y0 = 1/n
a = k*y0
g(x) = y0*x/(x+a)

set xlabel '$t$'

set yrange [:10100]
set xtics 0.25

unset key

plot filename1 u 1:2 w lp lc -1 lt 7 notitle '$z$',\
f(x) lc 4 lw 2 notitle 

set xlabel '$x$'

set format y2 '$%g$'
set format y ''
set y2tics 20
set xtics 200

set xrange [-10:1010]
set yrange [-2:102]
set y2range [-2:102]

plot filename2 w lp lc -1 lt 7 notitle,\
g(x) lc 4 lw 2 notitle


unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
