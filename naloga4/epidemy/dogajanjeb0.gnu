#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf14d.tex"

set samples 10000
set key box right width 0.1 height .3 Left reverse invert samplen 0.5
set key box opaque

set key title '$\alpha = 0.75, \, \beta =0$' left

filename1 = 'epidemy/brez_zdravljenja/alfa100.txt'
filename2 = 'epidemy/brez_zdravljenja/alfa750.txt'
filename3 = 'epidemy/brez_zdravljenja/imuni01_alpha01.txt'
filename4 = 'epidemy/brez_zdravljenja/imuni01_alpha75.txt'

set style line 1 lc rgb '#66c2a5' lt 1 lw 3
set style line 2 lc rgb '#fc8d62' lt 1 lw 3
set style line 3 lc rgb '#8da0cb lt 1 lw 3' lt 1 lw 3

set style fill transparent solid 0.5 border
set yrange [0:1]

set xlabel '$t$'
set ylabel '$N$'

plot filename4 u 4:1 ls 1 w filledcurves y=0 title '$D$',\
filename4 u 4:2 ls 2 w filledcurves y=0 title '$B$',\
filename4 u 4:3 ls 3 w filledcurves y=0 title '$I$'


unset term
set term dumb
unset out
set out '/dev/null'
