#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf9.tex"

set key box top right width 0.5 height 0.1 Left reverse invert samplen 0.5
set key opaque

set size square
set samples 10000
filename = 'co2_poli.txt'

set style line 1 lt 7 lw 3 ps 1.5 lc rgb '#d53e4f'
set style line 2 lt 7 lw 3 ps 1.5 lc rgb '#fc8d59'
set style line 3 lt 7 lw 3 ps 1.5 lc rgb '#fee08b'
set style line 4 lt 7 lw 3 ps 1.5 lc rgb '#99d594'
set style line 5 lt 7 lw 3 ps 1.5 lc rgb '#3288bd'
set style line 6 lt 7 lw 3 ps 1.5 lc rgb '#998ec3'


set style line 1 lt 7 lw 3 ps 1.5 lc rgb '#66c2a5'
set style line 2 lt 7 lw 3 ps 1.5 lc rgb '#fc8d62'
set style line 3 lt 7 lw 3 ps 1.5 lc rgb '#8da0cb'

#set style fill transparent solid 0.5

set xlabel '$\operatorname{Re}$'
set ylabel '$\operatorname{Im}$' 

set xtics 0.5
set mxtics 2
set ytics 0.5
set mytics 2

set grid lc 'grey'


set xrange [-1.1:1.1]
set yrange [-1.1:1.1]

f1(x) = sqrt(1-x**2)
f2(x) = -sqrt(1-x**2)

plot for [I=0:2] filename index I u 1:2 w p ls I+1 title columnheader,\
f1(x) lc -1 notitle,\
f2(x) lc -1 notitle

unset term
set term dumb
unset out
set out '/dev/null'