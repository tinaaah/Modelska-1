#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf6.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'energija_zveznih.txt'

#set yrange [-18.5:0.5]

#set grid lc 'grey' dt 1

set style line 1 lc rgb '#2166ac' lt 7 lw 1 ps .5
set style line 2 lc rgb '#67a9cf' lt 7 lw 1 ps .5
set style line 3 lc rgb '#d1e5f0' lt 7 lw 1 ps .5
set style line 4 lc rgb '#fddbc7' lt 7 lw 1 ps .5
set style line 5 lc rgb '#ef8a62' lt 7 lw 1 ps .5
set style line 6 lc rgb '#b2182b' lt 7 lw 1 ps .5
#set xrange [0:1]

maks = "519, 761, 12101, 35095, 59713, 90372"


#set key title '$E_{pr}$'
#plot filename every :::5::5 u ($1/90372):2 ls 6 w lines title '$T=5$',\
#filename every :::5::5 u ($1/90372):2 ls 6 w lines title '$T=5$',\
#filename every :::4::4 u ($1/59713):2 ls 5 w lines title '$T=1$',\
#filename every :::3::3 u ($1/35095):2 ls 4 w lines title '$T=0.5$',\
#filename every :::2::2 u ($1/12101):2 ls 3 w lines title '$T=0.25$',\
#filename every :::1::1 u ($1/761):2 ls 2 w lines title '$T=0.1$',\
#filename every :::0::0 u ($0/519):2 ls 1 w lines title '$T=0$' 

#set key title '$E_{pot}$'
#plot filename every :::5::5 u ($1/90372):3 ls 6 w lines title '$T=5$',\
#filename every :::4::4 u ($1/59713):3 ls 5 w lines title '$T=1$',\
#filename every :::3::3 u ($1/35095):3 ls 4 w lines title '$T=0.5$',\
#filename every :::2::2 u ($1/12101):3 ls 3 w lines title '$T=0.25$',\
#filename every :::1::1 u ($1/761):3 ls 2 w lines title '$T=0.1$',\
#filename every :::0::0 u ($0/519):3 ls 1 w lines title '$T=0$'

#set key title '$E$'
#plot filename every :::5::5 u ($1/90372):4 ls 6 w lines title '$T=5$',\
#filename every :::4::4 u ($1/59713):4 ls 5 w lines title '$T=1$',\
#filename every :::3::3 u ($1/35095):4 ls 4 w lines title '$T=0.5$',\
#filename every :::2::2 u ($1/12101):4 ls 3 w lines title '$T=0.25$',\
#filename every :::1::1 u ($1/761):4 ls 2 w lines title '$T=0.1$',\
#filename every :::0::0 u ($0/519):4 ls 1 w lines title '$T=0$'

set xrange [0:12100]
plot filename every :::2::2 u 1:2 ls 6 lc 4  w lines title '$E_{pr}$',\
filename every :::2::2 u 1:3 ls 6 lc 6 w lines title '$E_{pot}$',\
filename every :::2::2 u 1:4 ls 6 lc 7 w lines title '$E$'

unset term
set term dumb
unset out
set out '/dev/null'
