#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf7.tex"

set key box top right width -0.5 height 0.1 Left reverse invert samplen 0.5
# set key opaque

#set samples 10000
filename1 = 'co2_p.txt'
filename2 = 'co2_n.txt'

set style line 1 lt 7 lw 3 ps .5 lc rgb '#d53e4f'
set style line 2 lt 7 lw 3 ps .5 lc rgb '#fc8d59'
set style line 3 lt 7 lw 3 ps .5 lc rgb '#fee08b'
set style line 4 lt 7 lw 3 ps .5 lc rgb '#99d594'
set style line 5 lt 7 lw 3 ps .5 lc rgb '#3288bd'
set style line 6 lt 7 lw 3 ps .5 lc rgb '#998ec3'

#set style fill transparent solid 0.5

set ylabel '$\mathrm{P(\omega)}$'
set xlabel '$\omega$' 

set logscale y
set format y "$10^{%L}$"
set ytics add ('$1$' 1)

set xtics 0.1
set mxtics 2

plot for [I=1:5] filename1 u ($0/512):I w l ls I title columnheader,\
filename1 u ($0/512):6 w l lc -1 lw 3 title '$\text{FFT + Hann}$'

# plot for [I=0:5] filename2 index I u 1:2 w l ls I+1 title columnheader(2),\
# filename2 index 6 u 1:2 w l lc -1 lw 3 title '$\text{FFT + Hann}$'

unset term
set term dumb
unset out
set out '/dev/null'
