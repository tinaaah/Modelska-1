#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf12.tex"    #3 grafi za vsak plot posebej

set key box top right width 0.01 height 0.1 Left reverse invert samplen 1
set boxwidth -2
set key opaque

set title '$\Delta t = 0.01$'

set samples 10000
filename = 'loceni250.txt'
stats filename every ::1 nooutput
zad = STATS_blocks-2	#predzadnji blok

set yrange [0:]

f(x) = 250 * exp(-1.0*x)

set style line 1 lc rgb '#4d4d4d' lt 7 lw 1 ps .5
set style line 2 lc rgb '#91cf60' lt 7 lw 3 ps .5

#plot for [I=0:STATS_blocks-1]\
#    filename i I u 1:2 w l ls 1 notitle columnheader(1)

plot filename every ::1:0::99 w l ls 1 notitle, \
filename every ::1:100::100 w l ls 2 title '$\bar{N}$'


unset term
set term dumb
unset out
set out '/dev/null'