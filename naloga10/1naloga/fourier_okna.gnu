#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf5b.tex"

set key box top right Left reverse invert samplen 1 width -1
set key opaque

set samples 10000
filename1 = 'eksponent/cel_spekter.txt'
filename2 = 'bartlett/cel_spekter.txt'
filename3 = 'hann/cel_spekter.txt'
filename4 = 'welch/cel_spekter.txt'
filename5 = 'brez_okna/moc.txt'

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lt 7 lw 3 ps 1 lc rgb '#fc8d62'
set style line 2 lt 7 lw 3 ps 1 lc rgb '#8da0cb'
#set style fill transparent solid 0.5

set xlabel '$\omega$'
set ylabel '$|f|^2$'

set logscale y 
set format y '$10^{%L}$'
set ytics add ('$1$' 1)

#plot filename1 u 3:1 w lines ls 2 title 'val2',\
#filename1 u 3:2 w lines ls 1 title 'val3'

set style line 1 lt 7 lw 3 ps 1 lc rgb '#8dd3c7'
set style line 2 lt 7 lw 3 ps 1 lc rgb '#ffffb3'
set style line 3 lt 7 lw 3 ps 1 lc rgb '#bebada'
set style line 4 lt 7 lw 3 ps 1 lc rgb '#fb8072'
set style line 5 lt 7 lw 3 ps 1 lc rgb '#80b1d3'

plot filename1 u 3:1 w lines ls 4 title 'eksponent',\
filename2 u 3:1 w lines ls 2 title 'Bartlett',\
filename3 u 3:1 w lines ls 3 title 'Hann',\
filename4 u 3:1 w lines ls 1 title 'Welch',\
filename5 u 3:1 w lines ls 5 lc -1 title 'brez okna'

unset term
set term dumb
unset out
set out '/dev/null'
