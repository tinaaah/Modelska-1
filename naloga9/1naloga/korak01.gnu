#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex"    #3 grafi za vsak plot posebej

set key box top right width 0.01 height 0.1 Left reverse invert samplen 1
set boxwidth -2
set key opaque
unset key

set title '$\Delta t = 0.01$'

set samples 1000
filename = 'N250.txt'
stats filename every ::1 nooutput
zad = STATS_blocks-2	#predzadnji blok

f(x) = 250 * exp(-1.0*x)

set style line 1 lc rgb '#4d4d4d' lt 7 lw 1 ps .5
set style line 2 lc rgb '#91cf60' lt 7 lw 3 ps .5

#plot for [I=0:STATS_blocks-1]\
#    filename i I u 1:2 w l ls 1 notitle columnheader(1)

set yrange [0:250]
plot filename every ::1:0::99 w l ls 1 notitle, \
filename every ::1:100::100 w l ls 2 title '$\bar{N}$'

unset term
set term dumb
unset out
set out '/dev/null'
