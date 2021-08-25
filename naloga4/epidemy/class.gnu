#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf18c.tex"

set samples 10000
set key box right width 0.1 height .3 Left reverse invert samplen 0.5
set key box opaque

set key title '$\alpha = 0.5$' left
unset key

filename1 = 'epidemy/3razredi.txt'
filename2 = 'epidemy/6razredov.txt'
filename3 = 'epidemy/12razredov.txt'

set title '$N=12$'

#set label '$I_0=0$' at 15.5,0.68 front nopoint
#set label '$I_0=0.5$' at 26,0.24 front nopoint

set style line 1 lc 'midnight-blue' lt 1 lw 1
set style line 2 lc 'black' lt 1 lw 1

set style fill transparent solid 0.2 border
set yrange [0:]
#set xrange [0:100]
#set ytics 0.2

set xlabel '$t$'
set ylabel '$B$'

plot filename3 u 15:2 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:3 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:4 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:5 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:6 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:7 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:8 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:9 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:10 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:11 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:12 ls 1 w filledcurves y=0 title '$D$',\
filename3 u 15:13 ls 1 w filledcurves y=0 title '$D$'

#plot filename1 u 6:2 ls 1 w filledcurves y=0 title '$D$',\
#filename1 u 6:3 ls 1 w filledcurves y=0 title '$D$',\
#filename1 u 6:4 ls 1 w filledcurves y=0 title '$D$',\
#filename2 u 9:2 ls 2 w filledcurves y=0 title '$D$',\
#filename2 u 9:3 ls 2 w filledcurves y=0 title '$D$',\
#filename2 u 9:4 ls 2 w filledcurves y=0 title '$D$',\
#filename2 u 9:5 ls 2 w filledcurves y=0 title '$D$',\
#filename2 u 9:6 ls 2 w filledcurves y=0 title '$D$',\
#filename2 u 9:7 ls 2 w filledcurves y=0 title '$D$'


unset term
set term dumb
unset out
set out '/dev/null'
