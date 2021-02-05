#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf21.tex"    #3 grafi za vsak plot posebej

set key box top left width 0.01 height 0.5 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'porazdelitev_casov_250.txt'
filename2 = 'porazdelitev_casov_25.txt'

set style line 1 lc 4 lt 7 lw 3 ps .5
set style line 2 lc 6 lt 7 lw 3 ps .5

set xlabel '$\Delta t$'
set ylabel '$t_0$'

set logscale x

plot filename1 u 1:2 w lines ls 1 lc 4 title '$N_0 = 250$',\
filename2 u 1:2 w lines ls 2 lc 6 title '$N_0 = 25$'

unset term
set term dumb
unset out
set out '/dev/null'
