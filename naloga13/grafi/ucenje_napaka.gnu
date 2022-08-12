#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf10.tex"

set key box top right width -0.5 height 0.2 Left reverse invert samplen 1
set key opaque

set samples 10000

set grid lc 'gray' dt 2
filename = 'napaka_learning_rate.txt'

set xlabel 'povprečje $1000$ zaporednih'
set ylabel '$E$'

set style line 1 lt 7 lw 3 lc '#fed976' ps 1
set style line 2 lt 7 lw 3 lc '#feb24c' ps 1
set style line 3 lt 7 lw 3 lc '#fd8d3c' ps 1
set style line 4 lt 7 lw 3 lc '#f03b20' ps 1
set style line 5 lt 7 lw 3 lc '#bd0026' ps 1

#set logscale x
#set format x "$10^{%L}$"
#set xtics add ('$1$' 1, '$10$' 10)
#set ytics 0.2
set yrange [:0.7]

plot filename every :::0::0 u 1:2 w lp ls 1 title '$\eta = 10^{-6}$',\
	   '' every :::1::1 u 1:2 w lp ls 2 title '$\eta = 10^{-5}$',\
	   '' every :::2::2 u 1:2 w lp ls 3 title '$\eta = 10^{-4}$',\
	   '' every :::3::3 u 1:2 w lp ls 4 title '$\eta = 10^{-3}$',\
	   '' every :::4::4 u 1:2 w lp ls 5 title '$\eta = 10^{-2}$'

unset term
set term dumb
unset out
set out '/dev/null'
