#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1b.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 left Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = '../kalman_cartesian_data.dat' 
filename2 = '../kalman_cartesian_kontrola.dat' 
filename3 = 'trajektorija.txt'
filename4 = 'primerjava_napak.txt'

#set style fill transparent solid 0.25 

#plot filename2 using 1:3 lc 4 lt 7 ps .5 notitle,\
#filename3 using 1:3 lc 6 lt 7 ps .5  notitle



set ylabel '$y(t)$'
#set ytics 4000
#set ytics 2000
#set mytics 2

set xrange [0:2000]
set xlabel '$x(t)$'
#set xtics 10000
#set xtics 2000
#set mxtics 2

set grid lc 'grey'

plot filename2 using 2:3 w lines lc 8 lt 7 lw 2 title 'Kontrola',\
filename3 using 2:3 w lines lc 2 lt 7 lw 2 title 'Kalman'

unset term
set term dumb
unset out
set out '/dev/null'
