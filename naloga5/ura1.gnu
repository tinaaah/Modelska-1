#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf10.tex" 

set key box width 2 height 0.5 reverse samplen 1 Left
set key opaque

filename = 'ura1.txt'

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set xrange [0:5]
set yrange [-0.025:1.05]
set y2range [-0.025:1.05]

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

plot filename u 5:1 every :::0::0 w l lc 7 lw 3 title '$x$',\
filename u 5:2 every :::0::0 w l lc 4 lw 3 title '$y$',\
filename u 5:3 every :::0::0 w l lc 6 lw 3 title '$z$',\
filename u 5:4 every :::0::0 w l lc -1 lw 3 title '$w$'


unset key
set format y ''
set format y2 '$%g$'
set y2tics 0.2

plot filename u 5:1 every :::1::1 w l lc 7 lw 3 title '$x$',\
filename u 5:2 every :::1::1 w l lc 4 lw 3 title '$y$',\
filename u 5:3 every :::1::1 w l lc 6 lw 3 title '$z$',\
filename u 5:4 every :::1::1 w l lc -1 lw 3 title '$w$'

unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
