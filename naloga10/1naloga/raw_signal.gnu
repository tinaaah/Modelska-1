#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1b.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'val2.dat'
filename2 = 'val3.dat'

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lt 7 lw 2 ps 1 lc rgb '#66c2a5'
set style line 2 lt 7 lw 2 ps 1 lc rgb '#fc8d62'
set style line 3 lt 7 lw 2 ps 1 lc rgb '#8da0cb'
#set style fill transparent solid 0.5

set xtics 0.2
set xlabel '$t$'
set ylabel '$f(t)$'

unset key
#plot filename1 u ($0/512):1 w lines ls 3 

plot filename2 u ($0/512):1 w lines ls 2 

unset term
set term dumb
unset out
set out '/dev/null'
