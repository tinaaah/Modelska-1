#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf4.tex"

set key box top left width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000

#set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

bartlett(x) = 1 - abs(x-512/2)/(512/2)
welch(x) = 1 - ((x-512/2)/(512/2))**2
Hann(x) = sin(pi*x/512)**2
eksponent(x) = exp( - abs(x-512/2)/alpha)
alpha = (512/2)/(60/8.69)

set style fill transparent solid 0.6

set xlabel '$x$'
set ylabel 'amplituda'

set style line 1 lt 7 lw 3 ps 1 lc rgb '#8dd3c7'
set style line 2 lt 7 lw 3 ps 1 lc rgb '#ffffb3'
set style line 3 lt 7 lw 3 ps 1 lc rgb '#bebada'
set style line 4 lt 7 lw 3 ps 1 lc rgb '#fb8072'
set style line 5 lt 7 lw 3 ps 1 lc rgb '#80b1d3'

set xrange [0:512]

plot welch(x) with filledcurves ls 1 title 'Welch',\
Hann(x) with filledcurves ls 3 title 'Hann',\
bartlett(x) with filledcurves ls 2 title 'Bartlett',\
eksponent(x) with filledcurves ls 4 title 'eksponent'

unset term
set term dumb
unset out
set out '/dev/null'
