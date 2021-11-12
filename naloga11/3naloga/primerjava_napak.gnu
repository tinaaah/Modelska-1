#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf9a.tex"    #3 grafi za vsak plot posebej
set out "graf9b.tex"    #3 grafi za vsak plot posebej
#set out "graf9c.tex"    #3 grafi za vsak plot posebej
#set out "graf9d.tex"    #3 grafi za vsak plot posebej

set key box width -1 height 0.1 Left reverse invert samplen 1
#set key title 'Vsak korak' 'Vsak korak in vsak 5. korak' 'Vsak 5. korak in vsak 10. korak'
set key opaque

set samples 10000
filename0 = '../kalman_cartesian_kontrola.dat'
filename1 = 'odstopanje_meritve.txt'
filename2 = 'proba.txt'
filename3 = 'napake.txt'

#set style fill transparent solid 0.25 

set xlabel '$t$'

set ytics 40
set mytics 2
set grid lc 'grey'

#set ylabel '$\vec{x}_{\text{pravi}}-x^+$'
#set key box title '$x$ koordinata'

#plot filename1 using 1:2 w lines lc -1 lw 2 title 'Meritev',\
#filename3 using 1:2 w lines lc 4 lw 2 title 'Akcelerometer'

set ylabel '$\vec{y}_{\text{pravi}}-y^+$'
set key box title '$y$ koordinata'

plot filename1 using 1:3 w lines lc -1 lw 2 title 'Meritev',\
filename3 using 1:3 w lines lc 4 lw 2 title 'Akcelerometer'

#set logscale y
#set format y '$10^{%L}$'
#set ytics add ('$1$' 1)

#set key box title '$v_x$'
#set ylabel '$ ||(v_x - v_{x, \text{pravi}}) / v_{x,\text{pravi}}||$'

#plot filename3 u 1:4 w lines lc 4 lw 2 title 'Akcelerometer'

#set key box title '$v_y$'
#set ylabel '$ ||(v_y - v_{y, \text{pravi}}) / v_{y,\text{pravi}}||$'

#plot filename3 u 1:5 w lines lc 4 lw 2 title 'Akcelerometer'

unset term
set term dumb
unset out
set out '/dev/null'
