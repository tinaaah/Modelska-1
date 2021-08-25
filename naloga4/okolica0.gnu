#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader  #size 12.5cm,10cm
set out "graf5.tex" 


set key box left width 0.8 height .1 Left reverse invert samplen 0.5
set key box opaque
filename = 'okolica0.txt'

if (!exists("MP_LEFT"))   MP_LEFT = .15
if (!exists("MP_RIGHT"))  MP_RIGHT = .9
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.05

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

#set format y "%.1f"


#fff7ec','#fee8c8','#fdd49e','#fdbb84','#fc8d59','#ef6548','#d7301f','#b30000','#7f0000'
set style line 1 lc rgb '#ffff7f' lt 1 lw 1
set style line 2 lc rgb '#fee8c8' lt 1 lw 1
set style line 3 lc rgb '#fdd49e' lt 1 lw 1
set style line 4 lc rgb '#fdbb84' lt 1 lw 1
set style line 5 lc rgb '#fc8d59' lt 1 lw 1
set style line 6 lc rgb '#ef6548' lt 1 lw 1
set style line 7 lc rgb '#d7301f' lt 1 lw 1
set style line 8 lc rgb '#b30000' lt 1 lw 1
set style line 9 lc rgb '#7f0000' lt 1 lw 1
set style line 10 lc rgb '#a84020' lt 1 lw 1
set style line 11 lc rgb '#9e2b15' lt 1 lw 1
set style line 12 lc rgb '#95150b' lt 1 lw 1
set style line 13 lc rgb '#8b0000' lt 1 lw 1

set ylabel 'zajci'
set format y '%g'
set xlabel '$\tau$'
set ytics 4

set xrange [0:12]


plot filename u 3:1 every :::1::1 w l lc 2 lw 2 title '$z_0=0,75$',\
filename u 3:1 every :::2::2 w l lc 6 lw 2 title '$z_0=0,5$',\
filename u 3:2 every :::3::3 w l lc 4 lw 2 title '$z_0=0,25$',\
filename u 3:1 every :::0::0 w l lc 1 lw 2 title '$z_0=0,1$',\
filename u 3:1 every :::4::4 w l lc 7 lw 2 title '$z_0=0,01$',\
filename u 3:1 every :::5::5 w l lc 5 lw 2 title '$z_0=0,001$'

set ylabel ''
set ytics format ''

set y2label 'lisice' offset -1
set format y2 '%g'
set y2tics 4



plot filename u 3:2 every :::1::1 w l lc 2 lw 2 title '$l_0=0,75$',\
filename u 3:2 every :::2::2 w l lc 6 lw 2 title '$l_0=0,5$',\
filename u 3:2 every :::3::3 w l lc 4 lw 2 title '$l_0=0,25$',\
filename u 3:2 every :::0::0 w l lc 1 lw 2 title '$l_0=0,1$',\
filename u 3:2 every :::4::4 w l lc 7 lw 2 title '$l_0=0,01$',\
filename u 3:2 every :::5::5 w l lc 5 lw 2 title '$l_0=0,001$'



unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
