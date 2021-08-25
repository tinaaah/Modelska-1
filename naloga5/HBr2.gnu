#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf10.tex" 

set key box width 0.8 height 0.5 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename = 'kislina2.txt'

set xlabel '$\log_{10}\tau$'
set ylabel "$x$"
set xtics 0.75
set xrange [-2:2]

set key top left

#set logscale y
plot filename u (log10($4)):1 every :::4::4 w l lc 3 lw 3 title '$z_0/x_0 = 100$'
#filename u (log10($4)):1 every :::1::1 w l lc 6 lw 3 title '$z_0/x_0 = 1$',\
#filename u (log10($4)):1 every :::2::2 w l lc 4 lw 3 title '$z_0/x_0 = 3$'
#unset logscale y

set y2label "$y$"
set ylabel ""
set format y ""
set format y2 "$%g$"
set y2tics 0.2

set key bottom left
plot filename u (log10($4)):2 every :::0::0 w l lc 7 lw 3 title '$z_0/x_0 = 0,5$',\
filename u (log10($4)):2 every :::1::1 w l lc 6 lw 3 title '$z_0/x_0 = 1$',\
filename u (log10($4)):2 every :::2::2 w l lc 4 lw 3 title '$z_0/x_0 = 3$',\
filename u (log10($4)):2 every :::3::3 w l lc 2 lw 3 title '$z_0/x_0 = 20$',\
filename u (log10($4)):2 every :::4::4 w l lc 3 lw 3 title '$z_0/x_0 = 100$'


unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
