#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf47.tex"

set key box top right width 0.5 height 0.1 Left reverse invert samplen 0.5
set key opaque

#set samples 10000
filename = 'test_5.txt'
# filename = 'test_2.txt'

set style line 1 lt 7 lw 3 ps .5 lc rgb '#d7191c'
set style line 2 lt 7 lw 3 ps .5 lc rgb '#fdae61'
set style line 3 lt 7 lw 3 ps .5 lc rgb '#abdda4'
set style line 4 lt 7 lw 3 ps .5 lc rgb '#2b83ba'

#set style fill transparent solid 0.5

set ylabel '$\mathrm{P(\omega)}$'
set xlabel '$\omega$' 

set logscale y
set format y "$10^{%L}$"
set ytics add ('$1$' 1)
# set yrange [10e-6:]

# set xtics 0.1
# set mxtics 2

# plot filename u 1:2 w l lc -1 lw 3 title 'FFT + Hann',\
# for [I=3:6] filename u 1:I w l ls I-2 title columnheader

set xrange [1.5:2.5]

plot for [I=3:6] filename u 1:I w l ls I-2 title columnheader

unset term
set term dumb
unset out
set out '/dev/null'