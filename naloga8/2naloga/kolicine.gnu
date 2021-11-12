#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf26.tex" 

set key box top right width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'izracun.txt'
filename2 = 'izracun2.txt'

set style line 1 lt 7 lw 2 lc rgb '#66c2a5' ps 1
set style line 2 lt 7 lw 2 lc rgb '#fc8d62' ps 1
set style line 3 lt 7 lw 2 lc rgb '#8da0cb' ps 1


set xlabel '$T$'

#set ylabel '$\langle E\rangle$'

#set arrow from 2.269185,-4.5 to 2.269185, -2 nohead lc 7 dt 4 lw 3
#plot filename using 5:1 every :::0::0 w points ls 1 title '$H=0$',\
#filename using 5:1 every :::1::1 w points ls 2 title '$H=0.25$',\
#filename using 5:1 every :::2::2 w points ls 3 title '$H=0.5$'

#set ytics 0.003
#set ylabel '$c$'

#set arrow from 2.269185,0 to 2.269185,0.015 nohead lc 7 dt 4 lw 3
#plot filename using 5:($2*10e4) every :::0::0 w points ls 1 title '$H=0$',\
#filename using 5:($2*10e4) every :::1::1 w points ls 2 title '$H=0.25$',\
#filename using 5:($2*10e4) every :::2::2 w points ls 3 title '$H=0.5$'

#set ylabel '$\langle S\rangle$'

#set arrow from 2.269185,-0.2 to 2.269185, 1 nohead lc 7 dt 4 lw 3
#plot filename using 5:3 every :::0::0 w points ls 1 title '$H=0$',\
#filename using 5:3 every :::1::1 w points ls 2 title '$H=0.25$',\
#filename using 5:3 every :::2::2 w points ls 3 title '$H=0.5$'

set ylabel '$\chi$'

set arrow from 2.269185,0 to 2.269185,0.03 nohead lc 7 dt 4 lw 3
plot filename using 5:($4*10e3) every :::0::0 w points ls 1 title '$H=0$',\
filename using 5:($4*10e4) every :::1::1 w points ls 2 title '$H=0.25$',\
filename using 5:($4*10e4) every :::2::2 w points ls 3 title '$H=0.5$'

unset term
set term dumb
unset out
set out '/dev/null'
