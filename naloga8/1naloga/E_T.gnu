#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf23.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'casE.txt'

#set yrange [-18.5:0.5]

set style line 1 lt 7 lw 2 ps .5

plot filename u 4:2 w lp ls 6 lc 4 title '$E_{\text{pr}}$',\
filename u 4:1 w lp ls 6 lc 6 title '$E_{\text{pot}}$',\
filename u 4:3 w lp ls 6 lc 7 title '$E$',\

#unset term
#set term dumb
#unset out
#set out '/dev/null'
