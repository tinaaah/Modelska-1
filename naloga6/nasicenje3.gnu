#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf3.tex"

set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

#set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename1 = 'obrat2.txt'

set xlabel '$x$'
set ylabel '$log_{10} \frac{y - y_m}{y}$'
set logscale y
set logscale x

plot filename1 u 3:1 w lp lc 4 lw 2 lt 7 title 'z napakami',\
filename1 u 3:2 w lp lc 6 lw 2 lt 7 title 'brez napak'

#unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
