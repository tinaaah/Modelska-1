#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf5.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque


set samples 10000
filename1 = 'sosedi_T.txt'
filename2 = 'poljubni_T.txt'
filename3 = 'zvezni_T.txt'

stats filename1 every ::1 name 'sosedi' nooutput
stats filename2 every ::1 name 'poljubni' nooutput
stats filename3 every ::1 name 'zvezni' nooutput

set style line 1 lc rgb '#2166ac' lt 7 lw 3 ps .5
set style line 2 lc rgb '#67a9cf' lt 7 lw 3 ps .5
set style line 3 lc rgb '#d1e5f0' lt 7 lw 3 ps .5
set style line 4 lc rgb '#fddbc7' lt 7 lw 3 ps .5
set style line 5 lc rgb '#ef8a62' lt 7 lw 3 ps .5
set style line 6 lc rgb '#b2182b' lt 7 lw 3 ps .5

set xtics format ''
set x2tics 4
set xtics 4
set mx2tics 4 
set mxtics 4 

set ytics 3
set mytics 3

set grid xtics mxtics ytics mytics lc 'grey' dt 1

set key title 'sosedi'
plot for [I=0:sosedi_blocks-1] filename1 i I u 1:2 w l ls I+1 title columnheader(1)

#set key title 'poljubni'
#plot for [I=0:poljubni_blocks-1] filename2 i I u 1:2 w l ls I+1 title columnheader(1)

#set key title 'zvezni nivoji'
#plot for [I=0:zvezni_blocks-1] filename3 i I u 1:2 w l ls I+1 title columnheader(1)

unset term
set term dumb
unset out
set out '/dev/null'
