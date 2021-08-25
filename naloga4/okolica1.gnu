#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader  #size 12.5cm,10cm
set out "graf4.tex" #grafi predstavljajo potek populacij pri začetnem 1 zajcu in 0.25 lisice


set key box width 0.8 height .1 Left reverse invert samplen 0.5
set key box opaque
filename = 'okolica1.txt'

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

#plot filename u 1:2 every :::0::0 w l ls 1 title 'p = 8',\
#filename u 1:2 every :::1::1 w l ls 2 title 'p = 4',\
#filename u 1:2 every :::2::2 w l ls 3 title 'p = 2',\
#filename u 1:2 every :::3::3 w l ls 4 title 'p = 1',\
#filename u 1:2 every :::4::4 w l ls 5 title 'p = 0,9',\
#filename u 1:2 every :::5::5 w l ls 6 title 'p = 0,7',\
#filename u 1:2 every :::6::6 w l ls 7 title 'p = 0,6',\
#filename u 1:2 every :::7::7 w l ls 8 title 'p = 0,5',\
#filename u 1:2 every :::8::8 w l ls 9 title 'p = 0,4'


set ylabel 'lisice, zajci'
set format y '%g'
set xlabel '$\tau$'

unset key

set xrange [0:15]
plot filename u 3:1 every :::0::0 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::0::0 w l lc 6 notitle 'lisice',\
filename u 3:1 every :::10::10 w l lc 4 notitle 'zajci',\
filename u 3:2 every :::10::10 w l lc 4 notitle 'lisice'
#filename u 3:1 every :::2::2 w l lc 3 notitle 'zajci',\
#filename u 3:2 every :::2::2 w l lc 3 notitle 'lisice',\
#filename u 3:1 every :::3::3 w l lc 4 notitle 'zajci',\
#filename u 3:2 every :::3::3 w l lc 4 notitle 'lisice',\
#filename u 3:1 every :::4::4 w l lc 5 notitle 'zajci',\
#filename u 3:2 every :::4::4 w l lc 5 notitle 'lisice',\
#filename u 3:1 every :::5::5 w l lc 6 notitle 'zajci',\
#filename u 3:2 every :::5::5 w l lc 6 notitle 'lisice',\
#filename u 3:1 every :::6::6 w l lc 7 notitle 'zajci',\
#filename u 3:2 every :::6::6 w l lc 7 notitle 'lisice',\
#filename u 3:1 every :::7::7 w l lc 8 notitle 'zajci',\
#filename u 3:2 every :::7::7 w l lc 8 notitle 'lisice',\
#filename u 3:1 every :::8::8 w l lc 9 notitle 'zajci',\
#filename u 3:2 every :::8::8 w l lc 9 notitle 'lisice',\
#filename u 3:1 every :::9::9 w l lc 10 notitle 'zajci',\
#filename u 3:2 every :::9::9 w l lc 10 notitle 'lisice',\

set ylabel ''
set ytics format ''
set xtics 0.05

set y2label 'lisice' offset -3
set format y2 '%g'
set y2tics 0.05
unset xrange
unset yrange
set xlabel 'zajci'

set xrange [0.94:1.06]
set yrange [0.94:1.06]

plot filename u 1:2 every :::0::0 w l ls 1 notitle 'p = 1,05',\
filename u 1:2 every :::1::1 w l ls 2 notitle 'p = 1,04',\
filename u 1:2 every :::2::2 w l ls 3 notitle 'p = 1,03',\
filename u 1:2 every :::3::3 w l ls 4 notitle 'p = 1,02',\
filename u 1:2 every :::4::4 w l ls 5 notitle 'p = 1,01',\
filename u 1:2 every :::5::5 w l ls 6 notitle 'p = 1',\
filename u 1:2 every :::6::6 w l ls 7 notitle 'p = 0,99',\
filename u 1:2 every :::7::7 w l ls 8 notitle 'p = 0,98',\
filename u 1:2 every :::8::8 w l ls 9 notitle 'p = 0,97',\
filename u 1:2 every :::9::9 w l ls 10 notitle 'p = 0,96',\
filename u 1:2 every :::10::10 w l ls 11 notitle 'p = 0,95'


unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
