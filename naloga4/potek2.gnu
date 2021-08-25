#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex" #grafi predstavljajo potek populacij pri začetnih 2 zajcih in 1 lisici

#set key box width 0.8 height .1 Left reverse invert samplen 0.5

filename = 'razmerje21.txt'

set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .1
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.05

set multiplot layout 3,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

set ylabel 'lisice, zajci'
set format y '%g'
set xlabel ''
set format x ""
set xtics 20

set title '$p = 8$' offset 0,-1
set ytics 1
set mytics 5
plot filename u 3:1 every :::0::0 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::0::0 w l lc 4 notitle 'lisice'

set title '$p = 2$' offset 0,-1
plot filename u 3:2 every :::2::2 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::0::0 w l lc 4 notitle 'lisice'

set xlabel '$\tau$'
set format x '%g'

set title '$p = 1$' offset 0,-1
plot filename u 3:1 every :::3::3 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::3::3 w l lc 4 notitle 'lisice'

set ylabel ""
set xlabel ""
set format x ""

unset ytics
set y2tics 2
set my2tics 5
set title '$p=0,9$' offset 0,-1
plot filename u 3:1 every :::4::4 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::4::4 w l lc 4 notitle 'lisice'

set title '$p=0,7$' offset 0,-1
plot filename u 3:1 every :::5::5 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::5::5 w l lc 4 notitle 'lisice'

set xlabel '$\tau$'
set xtics format '%g'

set title '$p=0,74$' offset 0,-1
plot filename u 3:1 every :::8::8 w l lc 6 notitle 'zajci',\
filename u 3:2 every :::8::8 w l lc 4 notitle 'lisice'


unset multiplot
unset term
set term dumb
unset out
set out '/dev/null'
