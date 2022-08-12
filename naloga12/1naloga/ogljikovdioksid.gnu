#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf6.tex"

set key box top right width -0.5 height 0.1 Left invert samplen 0.5
set key opaque
unset key

set grid lc 'grey'

#set samples 10000
filename = 'co2.txt'

set style line 1 lt 7 lw 3 ps .5 lc rgb '#fc8d59'
set style line 2 lt 7 lw 3 ps .5 lc rgb '#3288bd'

#set style fill transparent solid 0.5

set ylabel '$\ce{CO_2}$'
set xlabel '$t$' 

# plot filename u 1:2 w l ls 2 notitle
plot filename u 1:3 w l ls 2 notitle

unset term
set term dumb
unset out
set out '/dev/null'
