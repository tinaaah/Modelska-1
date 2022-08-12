#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf18.tex"

set key box top right width -2 height 0.1 Right invert samplen 0.5
# set key opaque

set size square
set samples 10000
filename = 'preslikava_val.txt'


set style line 1 lt 7 lw 3 ps 1.5 lc rgb '#66c2a5'

set style line 1 lt 7 lw 3 ps 1.5 lc rgb '#fc8d62'
set style line 2 lt 6 lw 3 ps 1.5 lc rgb '#fc8d62'
set style line 3 lt 7 lw 3 ps 1.5 lc rgb '#8da0cb'
set style line 4 lt 6 lw 3 ps 1.5 lc rgb '#8da0cb'


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

plot filename every :::0::0 u 1:2 w p ls 1 title '$p=5$',\
filename every :::1::1 u 1:2 w p ls 2 title 'preslikan $p=5$',\
filename every :::2::2 u 1:2 w p ls 3 title '$p=15$',\
filename every :::3::3 u 1:2 w p ls 4 title 'preslikan $p=15$',\
f1(x) lc -1 notitle,\
f2(x) lc -1 notitle

unset term
set term dumb
unset out
set out '/dev/null'