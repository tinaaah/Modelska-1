#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex"    #3 grafi za vsak plot posebej


#set key box width 2 height 0.1 Left reverse invert samplen 1
#set key opaque

set samples 10000
filename = 'primerjava.txt'

set style fill transparent solid 0.25 

plot filename every :::0::0 using ($3):($1) lc 3 smooth freq w boxes title '$\text{Konvolucija}$',\
filename every :::1::1 using ($3):($1) lc 7 smooth freq w boxes title '$\text{Box-Muller}$',\


unset term
set term dumb
unset out
set out '/dev/null'
