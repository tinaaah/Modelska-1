#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf2.tex"    #3 grafi za vsak plot posebej

set key box width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'moment.txt'

set style fill transparent solid 0.25 
#set xrange [-0.2:10.2]
#set arrow 1 from graph 0,first 0 to graph 1,first 0 nohead dt 3

#plot filename every 6::0 u 3:1:2 with yerrorbars ps .6 lt 7 lc 1 title '$J_{xx}$',\
#filename every 6::1 u 3:1:2 with yerrorbars ps .6 lt 7 lc 4 title '$J_{yy}$',\
#filename every 6::2 u 3:1:2 with yerrorbars ps .6 lt 7 lc 7 title '$J_{zz}$',\
#filename every 6::3 u 3:1:2 with yerrorbars ps .6 lt 7 lc 5 title '$J_{xy}$',\
#filename every 6::4 u 3:1:2 with yerrorbars ps .6 lt 7 lc 2 title '$J_{xz}$',\
#filename every 6::5 u 3:1:2 with yerrorbars ps .6 lt 7 lc 3 title '$J_{yz}$'

plot filename every 6::0 u 3:2 ps .6 lt 7 lc 6 title '$J_{xx}$'

plot filename every 6::0 u 3:2 ps .6 lt 7 lc 6 title '$J_{xx}$'


#unset term
#set term dumb
#unset out
#set out '/dev/null'
