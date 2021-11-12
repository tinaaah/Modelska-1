#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf7a.tex"    #3 grafi za vsak plot posebej
#set out "graf7b.tex"    #3 grafi za vsak plot posebej
#set out "graf7c.tex"    #3 grafi za vsak plot posebej
#set out "graf7d.tex"    #3 grafi za vsak plot posebej

set key box width -1 height 0.1 Left reverse invert samplen 1
#set key title 'Vsak korak' 'Vsak korak in vsak 5. korak' 'Vsak 5. korak in vsak 10. korak'
set key opaque

set samples 10000
filename1 = 'primerjava_napak.txt'
filename2 = 'proba.txt'

#set style fill transparent solid 0.25 

set xlabel '$t$'


#set ytics 40
#set mytics 2
#set grid lc 'grey'

#set ylabel '$\vec{x}_{\text{pravi}}-x^+$'
#set key box title '$x$ koordinata'
#plot filename1 every :::0::0 using 1:2 w lines lc 8 lw 2 title 'Meritve',\
#filename1 every :::0::0 using 1:6 w lines lc 7 lw 2 title 'Kalman$^s$',\
#filename1 every :::1::1 using 1:6 w lines lc 3 lw 2 title 'Kalman$^v$'

#set ylabel '$\vec{y}_{\text{pravi}}-y^+$'

#set key box title '$y$ koordinata'
#plot filename1 every :::0::0 using 1:3 w lines lc 8 lw 1 title 'Meritve',\
#filename1 every :::0::0 using 1:7 w lines lc 7 lw 2 title 'Kalman$^s$',\
#filename1 every :::1::1 using 1:7 w lines lc 3 lw 2 title 'Kalman$^v$'

set logscale y
set format y '$10^{%L}$'
set ytics add ('$1$' 1)

set key box title '$v_x$'
set ylabel '$ ||(v_x - v_{x, \text{pravi}}) / v_{x,\text{pravi}}||$'

plot filename1 every :::0::0 using 1:8 w lines lc 7 lw 2 title 'Kalman$^s$',\
filename1 every :::1::1 using 1:8 w lines lc 3 lw 2 title 'Kalman$^v$'

#set key box title '$v_y$'
#set ylabel '$ ||(v_y - v_{y, \text{pravi}}) / v_{y,\text{pravi}}||$'

#plot filename1 every :::0::0 using 1:9 w lines lc 7 lw 2 title 'Kalman$^s$',\
#filename1 every :::1::1 using 1:9 w lines lc 3 lw 2 title 'Kalman$^v$'

#unset term
#set term dumb
#unset out
#set out '/dev/null'
