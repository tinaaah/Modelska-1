#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf7.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,3 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename = 'binarna3.txt'

set yrange [-0.05:1]
set y2range [-0.05:1]
set xrange [0:21]

plot filename u 5:1 every :::0::0 w l lw 3 lc 1 title '$\mu = 1000$',\
filename u 5:1 every :::1::1 w l lw 3 lc 2 title '$\mu = 10$',\
filename u 5:1 every :::2::2 w l lw 3 lc 3 title '$\mu = 1$',\
filename u 5:1 every :::3::3 w l lw 3 lc 4 title '$\mu = 0,1$',\
filename u 5:1 every :::4::4 w l lw 3 lc 7 title '$\mu = 0,01$'


unset key
set format y ""
plot filename u 5:2 every :::0::0 w l lw 3 lc 1 title '$\mu = 1000$',\
filename u 5:2 every :::1::1 w l lw 3 lc 2 title '$\mu = 10$',\
filename u 5:2 every :::2::2 w l lw 3 lc 3 title '$\mu = 1$',\
filename u 5:2 every :::3::3 w l lw 3 lc 4 title '$\mu = 0,1$',\
filename u 5:2 every :::4::4 w l lw 3 lc 7 title '$\mu = 0,01$'

unset key
set format y2 '$%g$'
set y2tics 0.2
plot filename u 5:3 every :::0::0 w l lw 3 lc 1 title '$\mu = 1000$',\
filename u 5:3 every :::1::1 w l lw 3 lc 2 title '$\mu = 10$',\
filename u 5:3 every :::2::2 w l lw 3 lc 3 title '$\mu = 1$',\
filename u 5:3 every :::3::3 w l lw 3 lc 4 title '$\mu = 0,1$',\
filename u 5:3 every :::4::4 w l lw 3 lc 7 title '$\mu = 0,01$'



unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
