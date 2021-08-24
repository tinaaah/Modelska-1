#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf4.tex"

set grid lc 'grey'
filename = 'hrana4.txt'
set datafile separator '\t'
#set format y "$\%g\%\%$"

set boxwidth 0.5

#set style fill pattern 4 
set style fill solid 0.5

plot filename using ($0):($2/2000):xtic(1) with boxes lc 6 notitle,\
filename using ($0):($2/2000+0.03):(sprintf('%.2fg', $2)) with labels notitle

unset term
set term dumb
unset out
set out '/dev/null'
