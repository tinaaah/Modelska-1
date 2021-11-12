#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf6.tex"
#set out "graf7.tex"
#set out "graf8.tex"
set out "graf9.tex"
#set out "graf10.tex"
#set out "graf11.tex"

set key box top right Left reverse invert samplen 1 width -1
set key opaque

set samples 10000
filename1 = 'moci.txt'
filename2 = 'signal0.dat'
filename3 = 'fourier_signala.txt'
filename4 = 'signal1.dat'
filename5 = 'signal2.dat'
filename6 = 'signal3.dat'

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lt 7 lw 3 ps 1 lc rgb '#66c2a5'
set style line 2 lt 7 lw 3 ps 1 lc rgb '#fc8d62'
set style line 3 lt 7 lw 3 ps 1 lc rgb '#8da0cb'
set style line 4 lt 7 lw 3 ps 1 lc rgb '#e78ac3'
#set style fill transparent solid 0.5

set xlabel '$t$'
set ylabel '$u_0(t)$'
set xrange [:512]

#plot filename3 u 5:1 ls 1 w l title 'signal0'

set ylabel '$u_i(t)$'
plot filename3 u 5:4 w lines ls 4 title 'signal3',\
filename3 u 5:3 w lines ls 3 title 'signal2',\
filename3 u 5:2 w lines ls 2 title 'signal1',\
filename3 u 5:1 w lines ls 1 title 'signal0'


#set xlabel '$t$'
#set ylabel '$c(t)$'
#set xrange [:512]
#plot filename6 u 0:1 w lines ls 4 title 'signal3',\
#filename5 u 0:1 w lines ls 3 title 'signal2',\
#filename4 u 0:1 w lines ls 2 title 'signal1'

#set ylabel '$|C|^2$'
#set xlabel '$\omega$'
#set xrange [0:256]

#set logscale y 
#set format y '$10^{%L}$'
#set ytics add ('$1$' 1)

#plot filename1 u 5:1 w lines ls 1 title 'signal0'

#plot filename1 u 5:4 w lines ls 4 title 'signal3',\
#filename1 u 5:3 w lines ls 3 title 'signal2',\
#filename1 u 5:2 w lines ls 2 title 'signal1',\
#filename1 u 5:1 w lines ls 1 title 'signal0'


unset term
set term dumb
unset out
set out '/dev/null'
