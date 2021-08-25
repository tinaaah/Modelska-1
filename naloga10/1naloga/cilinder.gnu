#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'temp.txt'

set yrange [-18.5:0.5]

set xtics format ''
set x2tics 4
set xtics 4
set mx2tics 4
set mxtics 4

set ytics 3
set mytics 3

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1
set grid lc 'grey' dt 1

set style line 1 lt 7 lw 2 ps 1
set style fill transparent solid 0.5

plot filename every :::0::6 w lp ls 1 lc rgb '#5066c2a5' title 'diskretni nivoji (sosedi)',\
filename every :::14::20 w lp ls 1 lc rgb '#508da0cb' title 'diskretni nivoji (poljubni)',\
filename every :::7::13 w lp ls 1 lc rgb '#50fc8d62' title 'zvezni nivoji'

unset term
set term dumb
unset out
set out '/dev/null'
