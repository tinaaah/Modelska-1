#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf20a.tex"    #3 grafi za vsak plot posebej

set key box top center width 0.01 height 0.5 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'populacija25.txt'
filename2 = 'populacija250.txt'
stats filename1 every ::1 nooutput
stats filename2 every ::1 nooutput

#f(x) = 25 * exp(-1.0*x)

set style line 1 lc rgb '#0c2c84' lt 7 lw 3 ps .5
set style line 2 lc rgb '#225ea8' lt 7 lw 3 ps .5
set style line 3 lc rgb '#1d91c0' lt 7 lw 3 ps .5
set style line 4 lc rgb '#41b6c4' lt 7 lw 3 ps .5
set style line 5 lc rgb '#7fcdbb' lt 7 lw 3 ps .5
set style line 6 lc rgb '#c7e9b4' lt 7 lw 3 ps .5
set style line 7 lc rgb '#ffffcc' lt 7 lw 3 ps .5

set style fill transparent solid 0.5 noborder

set xlabel '$N$'
set ylabel 'verjetnost'

#plot filename u 1:2 every :::0::0 w lines

set title '$N=25$'
set xtics add ('$25$' 24)
set xrange [0:24]

plot for [I=0:STATS_blocks-1]\
    filename1 i I u 1:2 w filledcurves x1 ls I+1 title columnheader(1) #,\
    #f(x) ls 1 lw 4 lc rgb '#a50026' title '$N_0 \mathrm{e}^{-\beta t}$'

#set title '$N=250$'
#set xtics add ('$250$' 249)
#set xrange [0:249]

#plot for [I=0:STATS_blocks-1]\
#    filename2 i I u 1:2 w filledcurves x1 ls I+1 title columnheader(1) #,\
#    #f(x) ls 1 lw 4 lc rgb '#a50026' title '$N_0 \mathrm{e}^{-\beta t}$'


unset term
set term dumb
unset out
set out '/dev/null'
