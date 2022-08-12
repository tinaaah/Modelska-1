#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf12.tex"

set key box top right width -0.5 height 0.2 Left reverse invert samplen 1
set key opaque

set samples 10000

set grid lc 'gray' dt 2
filename = 'epohe.txt'

set xlabel 'število ponovitev'
set ylabel 'natančnost'

set style line 1 lt 7 lw 3 lc '#8da0cb' ps 1
set style line 2 lt 7 lw 3 lc '#fc8d62' ps 1

set yrange [0.9:1]
set ytics 0.02

plot filename u 1:2 w lp ls 1 title 'trening',\
filename u 1:3 w lp ls 2 title 'test'

unset term
set term dumb
unset out
set out '/dev/null'