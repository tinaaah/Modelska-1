#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf8.tex" ## Trening
set out "graf9.tex" ## Test

unset key
set tic scale 0
set size square

#set palette defined (0 '#ffffd9', 1 '#edf8b1', 2 '#c7e9b4', 3 '#7fcdbb', 4 '#41b6c4', 5 '#1d91c0', 6 '#225ea8', 7 '#253494', 8 '#081d58')
set palette defined (0 '#000000', 1 '#081d58', 2 '#253494', 3 '#225ea8', 4 '#1d91c0', 5 '#41b6c4', 6 '#7fcdbb', 7 '#c7e9b4', 8 '#edf8b1', 9 '#ffffd9')

#set title 'trening slike'
set title 'test slike'
set xlabel 'podatki' 
set ylabel 'rezultat mreže' offset -1,0

set xrange [-0.5:9.5]
set yrange [-0.5:9.5]

set xtics 1
set ytics 1

set logscale cb

set view map

#splot 'heatmap_trening.txt' matrix with image
splot 'heatmap_test.txt' matrix with image


unset term
set term dumb
unset out
set out '/dev/null'
