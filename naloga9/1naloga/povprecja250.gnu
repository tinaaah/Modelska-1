#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf5.tex"    #3 grafi za vsak plot posebej

set key box top right width 0.01 height 0.5 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'average250.txt'
stats filename every ::1 nooutput

f(x) = 250 * exp(-1.0*x)
set yrange [0:]

set style line 1 lc rgb '#252525' lt 7 lw 3 ps .5
set style line 2 lc rgb '#636363' lt 7 lw 3 ps .5
set style line 3 lc rgb '#969696' lt 7 lw 3 ps .5
set style line 4 lc rgb '#bdbdbd' lt 7 lw 3 ps .5
set style line 5 lc rgb '#d9d9d9' lt 7 lw 3 ps .5
set style line 6 lc rgb '#f7f7f7' lt 7 lw 3 ps .5

set logscale y

plot for [I=0:STATS_blocks-1]\
    filename i I u 1:2 w l ls I+1 title columnheader(1),\
    f(x) ls 1 lw 4 lc rgb '#91cf60' title '$N_0 \mathrm{e}^{-\beta t}$'

#plot for [I=0:STATS_blocks-1]\
#    filename i I u 1:(abs($2-f(x))/f(x)) w l ls I+1 title columnheader(1),\


unset term
set term dumb
unset out
set out '/dev/null'
