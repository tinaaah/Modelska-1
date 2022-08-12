#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf11.tex"    ## Funkciji 

set key box left width 2 height 0.2 Left reverse invert samplen 1
set key opaque
unset key

set samples 10000

filename='residual_deep_dream.txt'

set grid lc 'gray' dt 2

set ylabel 'napaka'
set xlabel 'korak'
set yrange [0:]
set ytics 0.2

plot filename u 1:($2/1.3) w l lc 2 lw 2 notitle

unset term
set term dumb
unset out
set out '/dev/null'