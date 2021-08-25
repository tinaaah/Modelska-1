#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex"    #3 grafi za vsak plot posebej

set key box width .8 height 0.5 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP


set samples 10000
filename = 'moment.txt'

set style fill transparent solid 0.25 
set xrange [-0.2:10.2]
#set arrow 1 from graph 0,first 0 to graph 1,first 0 nohead dt 3

plot filename every 6::0 u 3:1 ps .6 lt 7 lc 6 title '$J_{xx}$'

set yrange [0.00005:0.0005]
set y2range [0.00005:0.0005]
set format y ''
set format y2 '$%2.0t \!\cdot \!10^{%L}$'
set y2tics 0.0001

plot filename every 6::0 u 3:2 ps .6 lt 7 lc 6 title '$\sigma_{J_{xx}}$'

unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'