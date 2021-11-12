#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf13a.tex"    #3 grafi za vsak plot posebej
set out "graf13b.tex"    #3 grafi za vsak plot posebej

set key box width -1 height 0.1 Left reverse invert samplen 1
#set key title 'Vsak korak' 'Vsak korak in vsak 5. korak' 'Vsak 5. korak in vsak 10. korak'
set key opaque

set samples 10000
filename1 = 'napake.txt'

#set style fill transparent solid 0.25 

set xlabel '$t$'

set logscale y
set format y '$10^{%L}$'
set ytics add ('$1$' 1)

#set ylabel '$||P||$'

#plot filename1 every :::0::0 using 1:2 w lines lc 7 lw 2 title 'Kalman$^0$',\
#filename1 every :::1::1 using 1:2 w lines lc 2 lw 2 title 'Kalman$^1$'

set ylabel '$||K||$'

plot filename1 every :::0::0 using 1:3 w points lc 7 lt 7 ps .5 title 'Kalman$^0$',\
filename1 every :::1::1 using 1:3 w points lc 2 lt 7 ps .5 title 'Kalman$^1$'

unset term
set term dumb
unset out
set out '/dev/null'
