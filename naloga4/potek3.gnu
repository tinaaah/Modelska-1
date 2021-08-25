#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader  size 12.5cm,10cm
set out "graf3.tex" #graf predstavljajo fazni potek pri razmerju 1:0.25 in 2:1




filename1 = 'razmerje14.txt'
filename2 = 'razmerje21.txt'

if (!exists("MP_LEFT"))   MP_LEFT = .15
if (!exists("MP_RIGHT"))  MP_RIGHT = .9
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.05

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP


#fff7ec','#fee8c8','#fdd49e','#fdbb84','#fc8d59','#ef6548','#d7301f','#b30000','#7f0000'
set style line 1 lc rgb '#ffff7f' lt 1 lw 2
set style line 2 lc rgb '#fee8c8' lt 1 lw 2
set style line 3 lc rgb '#fdd49e' lt 1 lw 2
set style line 4 lc rgb '#fdbb84' lt 1 lw 2
set style line 5 lc rgb '#fc8d59' lt 1 lw 2
set style line 6 lc rgb '#ef6548' lt 1 lw 2
set style line 7 lc rgb '#d7301f' lt 1 lw 2
set style line 8 lc rgb '#b30000' lt 1 lw 2
set style line 9 lc rgb '#7f0000' lt 1 lw 2
set style line 10 lc rgb '#a84020' lt 1 lw 2
set style line 11 lc rgb '#9e2b15' lt 1 lw 2
set style line 12 lc rgb '#95150b' lt 1 lw 2
set style line 13 lc rgb '#8b0000' lt 1 lw 2


set ylabel 'lisice'
set xlabel 'zajci'

set title '$z_0=1$ in $l_0=0,25$' offset 0,-0.8
set xtics 0.5
set ytics 1

set label 1 at 0.6, 6.1 '$p=0,4$' front
set label 2 at 0.6, 1 '$p=8$' front

plot filename1 u 1:2 every :::0::0 w l ls 1 notitle '8',\
filename1 u 1:2 every :::1::1 w l ls 2 notitle '4',\
filename1 u 1:2 every :::2::2 w l ls 3 notitle '2',\
filename1 u 1:2 every :::3::3 w l ls 4 notitle '1',\
filename1 u 1:2 every :::4::4 w l ls 5 notitle '0,9',\
filename1 u 1:2 every :::5::5 w l ls 6 notitle '0,7',\
filename1 u 1:2 every :::6::6 w l ls 7 notitle '0,6',\
filename1 u 1:2 every :::7::7 w l ls 8 notitle '0,5',\
filename1 u 1:2 every :::8::8 w l ls 9 notitle '0,4'

set ylabel ''
#set format y ''

#set key box width 0.8 height .1 out Right samplen 1
unset key

set title '$z_0=2$ in $l_0=1$' offset 0,-0.8
set xtics 0.4

set label 1 at 0.8, 4.5 '$p=0,4$' front
set label 2 at 0.8, 1 '$p=8$' front

plot filename2 u 1:2 every :::0::0 w l ls 1 title '$8$',\
filename2 u 1:2 every :::1::1 w l ls 2 title '$4$',\
filename2 u 1:2 every :::2::2 w l ls 3 title '$2$',\
filename2 u 1:2 every :::3::3 w l ls 4 title '$1$',\
filename2 u 1:2 every :::4::4 w l ls 5 title '$0,9$',\
filename2 u 1:2 every :::5::5 w l ls 6 title '$0,7$',\
filename2 u 1:2 every :::6::6 w l ls 7 title '$0,6$',\
filename2 u 1:2 every :::7::7 w l ls 8 title '$0,5$',\
filename2 u 1:2 every :::8::8 w l ls 9 title '$0,4$'



unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
