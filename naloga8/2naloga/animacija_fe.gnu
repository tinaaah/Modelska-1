#!/usr/bin/gnuplot
set term png #colour solid rounded noheader size 20cm,18cm

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set size square

set xrange [0:200]
set yrange [0:200]

set samples 10000

filename1 = 'hlajenje_feromagneta.txt'
filename2 = 'hlajenje_antiferomagneta.txt'

set pm3d map

set autoscale fix
set palette defined (0 '#edf8b1', 1 '#2c7fb8')
set tics scale 0
unset cbtics
unset colorbox
unset key 
unset tics
unset border

do for [i=0:50] {
    temp = (50.-i)/10.0
    set output sprintf('ising%02.0f.png',50-i)
    set title sprintf('T = %2.1f', temp) 
    plot filename2 index i matrix with image
}

unset term
set term dumb
unset out
set out '/dev/null'
