#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf1.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'energija.txt'

set style line 1 lt 7 lw 2 ps .5

plot filename w points ls 1 lc 6 notitle


#unset term
#set term dumb
#unset out
#set out '/dev/null'
