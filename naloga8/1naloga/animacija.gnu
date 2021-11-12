#!/usr/bin/gnuplot
set terminal pngcairo size 350,262 enhanced font 'Verdana,10'

filename1 = 'gif_zvezni.txt'
filename2 = 'gif_sosedi.txt'
filename3 = 'gif_poljubni.txt'
unset key

system('mkdir -p proba')

stats filename1 name 'zvezni' nooutput
stats filename2 name 'sosedi' nooutput
stats filename3 name 'poljubni' nooutput

set xtics format ''
set x2tics 4
set xtics 4
set mx2tics 4 
set mxtics 4 

set ytics 3
set mytics 3

set grid ytics mytics x2tics mx2tics lc 'grey' dt 1

round(x) = x - floor(x) < 0.5 ? floor(x) : ceil(x)

set style line 1 lc rgb '#fc8d62' lt 7 lw 2 ps .5  #zvezni
set style line 2 lc rgb '#66c2a5' lt 7 lw 2 ps .5  #diskretni sosedi
set style line 3 lc rgb '#8da0cb' lt 7 lw 2 ps .5  #diskretni poljubni 

#Make sure there's no blank line at the end to use STATS_blank !!
do for [i=1:int(zvezni_blank)] {
    n1 = i-1
    n2 = round(int(sosedi_blank)/int(zvezni_blank)) * i - 1
    n3 = round(int(poljubni_blank)/int(zvezni_blank)) * i - 1
    #n3 = n2

    set output sprintf('proba/molekula%03.0f.png',i)
    plot filename1 every :::n1::n1 with linespoints ls 1 notitle,\
    filename2 every :::n2::n2 with linespoints ls 2 notitle,\
    filename3 every :::n3::n3 with linespoints ls 3 notitle
}

unset term
set term dumb
unset out
set out '/dev/null'
