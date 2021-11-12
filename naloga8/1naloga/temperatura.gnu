#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf6.tex"    #3 grafi za vsak plot posebej

set key box top right width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'proba.txt'

set xrange [0:]
set ytics 100

set style line 1 lt 7 lw 2 ps .5

plot filename u 4:1 w points pt 7 lc 4 ps .5 title '$E_{\text{pr}}$',\
filename u 4:2 w points pt 7 lc 6 ps .5 title '$E_{\text{pot}}$',\
filename u 4:3 w points pt 7 lc 7 ps .5 title '$E$'


#unset term
#set term dumb
#unset out
#set out '/dev/null'
