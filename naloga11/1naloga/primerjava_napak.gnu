#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf2a.tex"    #3 grafi za vsak plot posebej
#set out "graf2b.tex"    #3 grafi za vsak plot posebej
set out "graf2c.tex"    #3 grafi za vsak plot posebej
#set out "graf2d.tex"    #3 grafi za vsak plot posebej


set key box width -1 height 0.1 Left reverse invert samplen 1
#set key title 'Vsak korak' 'Vsak korak in vsak 5. korak' 'Vsak 5. korak in vsak 10. korak'
set key opaque

set samples 10000
filename1 = 'primerjava_napak.txt'
filename2 = 'primerjava_napak_hitrosti.txt'

#set style fill transparent solid 0.25 

set xlabel '$t$'
#set ylabel '$\vec{x}_{\text{pravi}}-x^+$'

#set ytics 40
#set mytics 2
#set grid lc 'grey'

#set key box title '$x$ koordinata'
#plot filename1 every :::0::0 using 1:2 w lines lc 8 lw 1 title 'Meritve',\
#filename1 every :::0::0 using 1:6 w lines lc 7 lw 2 title 'Kalman$^0$',\
#filename1 every :::1::1 using 1:6 w lines lc 2 lw 2 title 'Kalman$^1$'

#set key box title '$y$ koordinata'
#plot filename2 using 1:3 w lines lc 4 lt 7 lw 1 title 'Rešitv',\
#filename2 using 1:7 w lines lc 6 lt 7 lw 1 title 'Kalman'




set logscale y
set format y '$10^{%L}$'
set ytics add ('$1$' 1)

set key box title '$v_x$'
set ylabel '$ ||(v_x - v_{x, \text{pravi}}) / v_{x,\text{pravi}}||$'

plot filename2 every :::0::0 using 1:8 w lines lc 7 lw 2 title 'Kalman$^0$',\
filename2 every :::1::1 using 1:8 w lines lc 2 lw 2 title 'Kalman$^1$'

#set key box title '$v_y$'
#set ylabel '$ ||(v_y - v_{y, \text{pravi}}) / v_{y,\text{pravi}}||$'

#plot filename2 every :::0::0 using 1:9 w lines lc 7 lw 2 title 'Kalman$^0$',\
#filename2 every :::1::1 using 1:9 w lines lc 2 lw 2 title 'Kalman$^1$'

unset term
set term dumb
unset out
set out '/dev/null'
