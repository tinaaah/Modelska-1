#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf8d.tex"    #3 grafi za vsak plot posebej

set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'trajektorija.txt'
filename2 = '../kalman_cartesian_kontrola.dat'

#set style fill transparent solid 0.25 

#set xlabel '$x(t)$'
#set ylabel '$y(t)$'
#set xrange [0:2000]

#plot filename2 using 2:3 w lines lc -1 lt 7 lw 1 title 'Realno',\
#filename1 using 2:3 w lines lc 4 lt 7 lw 1 title 'Akcelerometer'

#set ylabel '$v_x$'
#set xlabel '$t$'
#plot filename2 using 1:4 w lines lc -1 lt 7 lw 2 title 'Realno',\
#filename1 using 1:4 w lines lc 4 lt 7 lw 2 title 'Akcelerometer'

#set ylabel '$v_y$'
#set xlabel '$t$'
#plot filename2 using 1:5 w lines lc -1 lt 7 lw 2 title 'Realno',\
#filename1 using 1:5 w lines lc 4 lt 7 lw 2 title 'Akcelerometer'

set ylabel '$v$'
set xlabel '$t$'

plot filename2 using 1:(sqrt($4**2+$5**2)) w lines lc -1 lt 7 lw 2 title 'Realno',\
filename1 using 1:(sqrt($4**2+$5**2)) w lines lc 4 lt 7 lw 2 title 'Akcelerometer'


#unset term
#set term dumb
#unset out
#set out '/dev/null'
