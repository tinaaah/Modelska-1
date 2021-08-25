#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"    #3 grafi za vsak plot posebej


#set key box width 2 height 0.1 Left reverse invert samplen 1
#set key opaque

set samples 10000
filename = 'konvolucija.txt'

set style fill solid 0.2

plot filename every :::0::0 using ($2):($1/1000) lc 7 smooth freq w boxes title 'N=1',\
filename every :::1::1 using ($2):($1/1000) lc 1 smooth freq w boxes title 'N=3',\
filename every :::2::2 using ($2):($1/1000) lc 3 smooth freq w boxes title 'N=6',\
filename every :::3::3 using ($2):($1/1000) lc 5 smooth freq w boxes title 'N=12'


unset term
set term dumb
unset out
set out '/dev/null'
