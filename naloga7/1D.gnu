#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf4.tex"    #3 grafi za vsak plot posebej


#set key box width 2 height 0.1 Left reverse invert samplen 1
#set key opaque

set samples 10000
filename1 = '1Dhistogram.txt' 
filename2 = '3Dhistogram.txt' 

set style fill transparent solid 0.25 
set xrange [0:25]

plot filename1 using ($2):($1/100000) lc 3 smooth freq w boxes title '$1D$' ,\
filename2 using ($2):($1/100000) lc 4 smooth freq w boxes title '$3D$' 


unset term
set term dumb
unset out
set out '/dev/null'
