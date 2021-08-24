#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"

set grid lc 'grey'
filename = 'hrana.txt'
#set format y "$\%g\%\%$"

set boxwidth 0.8

#set style fill pattern 4 
set style fill solid 0.5

plot filename using 0:($2/2000):xtic(1) with boxes lc 6 notitle,\
filename using 0:($2/2000+0.03):(sprintf('%05.2fg', $2)) with labels notitle

unset term
set term dumb
unset out
set out '/dev/null'
