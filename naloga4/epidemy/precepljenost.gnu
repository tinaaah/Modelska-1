#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf17b.tex"

set samples 10000
set key box right width 0.1 height .3 Left reverse invert samplen 0.5
set key box opaque

set key title '$\alpha = 0.5$' left
unset key

filename1 = 'epidemy/beta.txt'
filename2 = 'epidemy/Imuni.txt'

set label '$I_0=0$' at 15.5,0.68 front nopoint
set label '$I_0=0.5$' at 24,0.3 front nopoint

#set label '$\beta=0.05$' at 16.4,0.42 front nopoint
#set label '$\beta=0.5$' at 20,0.01 front nopoint

set style line 1 lc 'midnight-blue' lt 1 lw 1
set style line 2 lc rgb '#f1a340' lt 1 lw 1

set style fill transparent solid 0.1 border
set yrange [0:]
set ytics 0.2
set xrange [0:50]

set xlabel '$t$'
set ylabel '$B(I_0)$'

plot filename2 every:2::0::9 u 4:2 ls 1 w filledcurves y=0 title '$D$'
#filename1 u 4:2 ls 2 w filledcurves y=0 title '$B$',\
#filename1 u 4:3 ls 3 w filledcurves y=0 title '$I$'


unset term
set term dumb
unset out
set out '/dev/null'
