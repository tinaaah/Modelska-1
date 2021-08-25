#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf13.tex" 

set key box width 2 height 0.5 reverse samplen 1 Left
set key opaque

filename = 'ura4.txt'

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,3 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

set xlabel '$\tau$'

set yrange [-0.01:1]


set logscale x
unset key

plot filename u 5:1 every :::0::0 w l lc 1 lw 3 title '$w=0,5$',\
filename u 5:1 every :::1::1 w l lc 6 lw 3 title '$w=1$',\
filename u 5:1 every :::2::2 w l lc 2 lw 3 title '$w=2,5$',\
filename u 5:1 every :::3::3 w l lc 5 lw 3 title '$w=5$',\
filename u 5:1 every :::4::4 w l lc 4 lw 3 title '$w=10$',\
filename u 5:1 every :::5::5 w l lc 7 lw 3 title '$w=20$'

set key
set format y ""
plot filename u 5:3 every :::0::0 w l lc 1 lw 3 title '$w=0,5$',\
filename u 5:3 every :::1::1 w l lc 6 lw 3 title '$w=1$',\
filename u 5:3 every :::2::2 w l lc 2 lw 3 title '$w=2,5$',\
filename u 5:3 every :::3::3 w l lc 5 lw 3 title '$w=5$',\
filename u 5:3 every :::4::4 w l lc 4 lw 3 title '$w=10$',\
filename u 5:3 every :::5::5 w l lc 7 lw 3 title '$w=20$'


set y2range [-0.005:0.505]
set yrange [-0.005:0.505]
unset key
set format y2 "$%g$"
set y2tics 0.1

plot filename u 5:2 every :::0::0 w l lc 1 lw 3 title '$w=0,5$',\
filename u 5:2 every :::1::1 w l lc 6 lw 3 title '$w=1$',\
filename u 5:2 every :::2::2 w l lc 2 lw 3 title '$w=2,5$',\
filename u 5:2 every :::3::3 w l lc 5 lw 3 title '$w=5$',\
filename u 5:2 every :::4::4 w l lc 4 lw 3 title '$w=10$',\
filename u 5:2 every :::5::5 w l lc 7 lw 3 title '$w=20$'

unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
