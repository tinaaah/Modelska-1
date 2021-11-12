#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf6a.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 left Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = '../kalman_cartesian_data.dat' 
filename2 = '../kalman_cartesian_kontrola.dat' 
filename3 = 'trajektorija.txt'
filename4 = 'primerjava_napak.txt'

#set style fill transparent solid 0.25 

#set xrange [0:2000]

set grid lc 'grey'

plot filename3 every :::0::0 using 2:3 w lines lc 7 lt 7 lw 2 title 'brez hitrosti',\
filename3 every :::1::1 using 2:3 w lines lc 11 lt 7 lw 2 title 'brez lokacije',\
filename2 using 2:3 w lines lc 8 lt 7 lw 2 title 'kontrola'

#unset term
#set term dumb
#unset out
#set out '/dev/null'
