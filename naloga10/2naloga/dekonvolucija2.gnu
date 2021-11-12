#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf12.tex"
#set out "graf13.tex"
#set out "graf14.tex"
set out "graf15.tex"

set key box top right Left reverse invert samplen 1 width 1
set key opaque

set samples 10000
filename1 = 'porezan_signal_n16.txt'
filename2 = 'porezan_signal_n25.txt'
filename3 = 'porezan_signal_n50.txt'
filename4 = 'porezan_signal_n100.txt'

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lt 7 lw 3 ps 1 lc rgb '#a6cee3'
set style line 2 lt 7 lw 3 ps 1 lc rgb '#1f78b4'
set style line 3 lt 7 lw 3 ps 1 lc rgb '#b2df8a'
set style line 4 lt 7 lw 3 ps 1 lc rgb '#33a02c'
set style line 5 lt 7 lw 3 ps 1 lc rgb '#fb9a99'
#set style fill transparent solid 0.5

set xlabel '$t$'
set xrange [:512]

#set ylabel '$u_0(t)$'
#plot filename4 u 5:1 w lines ls 1 title '$m=100$',\
#filename3 u 5:1 w lines ls 2 title '$m=50$',\
#filename2 u 5:1 w lines ls 3 title '$m=25$',\
#filename1 u 5:1 w lines ls 4 title '$m=16$'


set ylabel '$u_3(t)$'
plot filename3 u 5:4 w lines ls 1 title '$m=50$',\
filename2 u 5:4 w lines ls 2 title '$m=25$',\
filename1 u 5:4 w lines ls 3 title '$m=16$'

#set logscale y 
#set format y '$10^{%L}$'
#set ytics add ('$1$' 1)

unset term
set term dumb
unset out
set out '/dev/null'
