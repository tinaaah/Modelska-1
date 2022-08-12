#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
# set out "graf19.tex"
set out "graf20.tex"

set key box top right width -0.5 height 0.1 Left reverse invert samplen 0.5
set key opaque

#set samples 10000
filename1 = 'napake_val.txt'
filename2 = 'napake_val_p.txt'

set style line 1 lt 7 lw 3 ps 1.5 lc rgb '#ef8a62'
set style line 2 lt 7 lw 3 ps 1.5 lc rgb '#67a9cf'
#set style fill transparent solid 0.5

# set ylabel '$\Delta S_n$'
# set xlabel '$n$' 
# 
# set xrange[256:512]
# set logscale y
# 
# plot filename1 every :::0::0 u 0:(abs(($1-$2)/$1)) w l ls 1 title 'val2',\
# filename1 every :::1::1 u 0:(abs(($1-$2)/$1)) w l ls 2 title 'val3'

set ylabel 'vsota relativnih napak'
set xlabel '$p$' 

set ytics 400
set xtics 4

plot filename2 u 1:2 w lp ls 1 title 'val2',\
filename2 u 1:3 w lp ls 2 title 'val3'


unset term
set term dumb
unset out
set out '/dev/null'