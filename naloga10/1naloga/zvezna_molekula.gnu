#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf3.tex"    

set key box top center width 1 height 0.1 Left reverse samplen 1
set key opaque

set samples 10000
filename = 'zvezni_nivoji_temperatura.txt'

set yrange [-18.5:0.5]

set xtics format ''
set x2tics 4
set xtics 4
set mx2tics 4
set mxtics 4

set ytics 3
set mytics 3

set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lc rgb '#ffffcc' lt 7 lw 2 ps 1
set style line 2 lc rgb '#c7e9b4' lt 7 lw 2 ps 1
set style line 3 lc rgb '#7fcdbb' lt 7 lw 2 ps 1
set style line 4 lc rgb '#41b6c4' lt 7 lw 2 ps 1
set style line 5 lc rgb '#1d91c0' lt 7 lw 2 ps 1
set style line 6 lc rgb '#225ea8' lt 7 lw 2 ps 1
set style line 7 lc rgb '#0c2c84' lt 7 lw 2 ps 1

plot filename every :::0::0 w lp ls 7 title '$t=289 \, T=0$',\
filename every :::1::1 w lp ls 6 title '$t=558 \, T=0,1$',\
filename every :::2::2 w lp ls 5 title '$t=11746 \, T=0,25$',\
filename every :::3::3 w lp ls 4 title '$t=34998 \, T=0,5$',\
filename every :::4::4 w lp ls 3 title '$t=59642 \, T=1$',\
filename every :::9::9 w lp ls 2 title '$t=98994 \, T=50$',\
filename every :::10::10 w lp ls 1 title '$t=99500 \, T=100$'

#unset term
#set term dumb
#unset out
#set out '/dev/null'
