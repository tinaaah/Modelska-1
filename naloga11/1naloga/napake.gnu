#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf1.tex"    #3 grafi za vsak plot posebej


#set key box width 2 height 0.1 Left reverse invert samplen 1
#set key opaque

set samples 10000
filename1 = 'kovarianca.txt'

#set style fill transparent solid 0.25 

plot filename1 using 1:(sqrt($2)) lc 4 lt 7 ps .5 notitle,\
filename1 using 1:(sqrt($3)) lc 6 lt 7 ps .5 notitle,\
filename1 using 1:(($4)) lc 2 lt 7 ps .5 notitle


#unset term
#set term dumb
#unset out
#set out '/dev/null'
