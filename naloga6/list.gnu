#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf6.tex"    #3 grafi za vsak plot posebej


set key box top left width -1 height 0.1 Left reverse samplen 1
set key opaque

set samples 1000

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

#set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename1 = 'CdL3_linfit.norm'
set xrange [3520:3580]
set xtics 25

set ylabel '$log_{10}\Delta y$'
a = 0.27273756 
b = 0.7300619 
c = 0.55442989 
d = 0.44591204

plot filename1 u 1:(log10(abs($2-(a*$4+b*$5)))) w l lc 4 lw 2 title '1. vzorec',\
filename1 u 1:(log10(abs($3-(c*$4+d*$5)))) w l lc 6 lw 2 title '2. vzorec',\

#plot filename1 u 1:2 w l lc 7 lw 2 title '1. vzorec',\
#filename1 u 1:3 w l lc 4 lw 2 title '2. vzorec',\
#filename1 u 1:4 w l lc 5 lw 2 title '1. standard',\
#filename1 u 1:5 w l lc 1 lw 2 title '2. standard'

#unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
