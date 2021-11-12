#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex"
#set out "graf3a.tex"
#set out "graf3b.tex"

set key box top left width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'brez_okna/moc.txt'
filename2 = 'brez_okna/moc_polovica.txt'
filename3 = 'brez_okna/moc_cetrtina.txt'
filename4 = 'brez_okna/moc_osmina.txt'

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lt 7 lw 3 ps 1 lc rgb '#fc8d62'
set style line 2 lt 7 lw 3 ps 1 lc rgb '#8da0cb'
#set style fill transparent solid 0.5

set xlabel '$\omega$'
set ylabel '$|f|^2$'

set logscale y 
set format y '$10^{%L}$'
set ytics add ('$1$' 1)

plot filename1 u 3:1 w lines ls 2 title 'val2',\
filename1 u 3:2 w lines ls 1 title 'val3'

#set style line 1 lt 7 lw 3 ps 1 lc rgb '#d7191c'
#set style line 2 lt 7 lw 3 ps 1 lc rgb '#fdae61'
#set style line 3 lt 7 lw 3 ps 1 lc rgb '#abd9e9'
#set style line 4 lt 7 lw 3 ps 1 lc rgb '#2c7bb6'

#plot filename1 u 3:2 w lines ls 1 title '$N=512$',\
#filename2 u 3:2 w lines ls 2 title '$N=256$',\
#filename3 u 3:2 w lines ls 3 title '$N=128$',\
#filename4 u 3:2 w lines ls 4 title '$N=64$',

#plot filename1 u 3:1 w lines ls 1 title '$N=512$',\
#filename2 u 3:1 w lines ls 2 title '$N=256$',\
#filename3 u 3:1 w lines ls 3 title '$N=128$',\
#filename4 u 3:1 w lines ls 4 title '$N=64$',

unset term
set term dumb
unset out
set out '/dev/null'
