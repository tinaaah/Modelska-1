#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf3.tex"    #3 grafi za vsak plot posebej

set key box right top width -0.5 height 0.4 Left reverse invert samplen 1
#set key opaque

set samples 10000
filename = 'porazdelitev_podatkov.txt'
stats filename every ::3 nooutput

set grid lc 'black'
set xlabel 'števka'
set ylabel 'delež'

set style fill transparent solid 0.5
set style line 1 lt 7 lw 2 lc '#8da0cb' ps .5 
set style line 2 lt 7 lw 2 lc '#fc8d62' ps .5 

#set yrange [0:]
#set xrange [-0.5:9.5]
#set xtics 1

boxwidth=0.4

set boxwidth 0.4 absolute
set style data boxes
set yrange [0:]
set xrange [-0.5:9.5]
set xtics 1

#plot for [I=0:STATS_blocks-1]\
#    filename i I u ($2):($1/10000) ls I+1 smooth freq w boxes title columnheader(1)

plot filename u ($1-boxwidth/2):($2/60000) ls 1 title "trening",\
filename u ($1+boxwidth/2):($3/10000) ls 2 title "test"

unset term
set term dumb
unset out
set out '/dev/null'
