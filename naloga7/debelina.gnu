#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf7.tex"    #3 grafi za vsak plot posebej

set key box width 1 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

set samples 10000
filename1 = 'debelina_1D.txt'
filename2 = 'debelina_3D.txt'
filename3 = 'debelina_razlika.txt'

set style fill transparent solid 0.25 
set xrange [-0.2:5.2]

plot filename1 u 3:1 ps .5 lt 7 lc 3 title '$T_1$',\
filename2 u 3:1 ps .5 lt 6 lc 4 title '$T_3$'

set yrange [:1e-5]
set y2range [:1e-5]
set format y ''
set format y2 '$%2.0t \cdot 10^{%L}$'
set y2tics 2*1e-6

set y2tics add ('$0$' 0)

plot filename3 u 5:($1/$3) ps .5 lt 7 lc -1 title '$ |T_1 - T_3| $',

unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
