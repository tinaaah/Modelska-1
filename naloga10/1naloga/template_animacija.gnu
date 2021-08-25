#!/usr/bin/gnuplot
set terminal pngcairo size 350,262 enhanced font 'Verdana,10'

filename = 'gif_poljubni.txt'
unset key

system('mkdir -p pngrac')

stats filename name 'poljubni' nooutput

set xtics format ''
set x2tics 4
set xtics 4
set mx2tics 4 
set mxtics 4 

set ytics 3
set mytics 3

set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

set style line 1 lc rgb '#fc8d62' lt 7 lw 2 ps .5  #zvezni
set style line 2 lc rgb '#66c2a5' lt 7 lw 2 ps .5  #diskretni sosedi
set style line 3 lc rgb '#8da0cb' lt 7 lw 2 ps .5  #diskretni poljubni 

#Make sure there's no blank line at the end to use STATS_blank !!
do for [i=1:int(poljubni_blank)] {
    n = i-1
    set output sprintf('pngrac/molekula%03.0f.png',i)

    plot filename every :::n::n with linespoints ls 3 notitle
}

unset term
set term dumb
unset out
set out '/dev/null'
