#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf9.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.5 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'bin2.txt'
stats filename every ::1 nooutput

set title '$N_0 = 250$'

set style fill transparent solid 0.5

set style line 6 lc rgb '#e41a1c' lt 7 lw 2 ps .5
set style line 5 lc rgb '#377eb8' lt 7 lw 2 ps .5
set style line 4 lc rgb '#4daf4a' lt 7 lw 2 ps .5
set style line 3 lc rgb '#984ea3' lt 7 lw 2 ps .5
set style line 2 lc rgb '#ff7f00' lt 7 lw 2 ps .5
set style line 1 lc rgb '#ffff33' lt 7 lw 2 ps .5



plot for [I=0:STATS_blocks-1]\
    filename i I u ($2):($1/10000) ls I+1 smooth freq w boxes title columnheader(1)


unset term
set term dumb
unset out
set out '/dev/null'
