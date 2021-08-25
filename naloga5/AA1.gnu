#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf3.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename = 'binarna1.txt'

set ylabel "$a^*$"
set xlabel '$\tau$'

#set title 'Spreminjanje a in b (in c) s~časom'
#set xrange [0:65]
#set yrange [-.025:]
#set xtics 20
set ytics 0.2

#plot filename u 5:1 every :::1::1 w l lw 3 lc 8 title '$a$',\
#filename u 5:2 every :::1::1 w l lw 3 lc 1 title '$a^*$',\
#filename u 5:3 every :::1::1 w l lw 3 lc 3 title '$b,c$',\

#plot filename u 5:1 every :::0::0 w l lw 3 lc 4 title '$\lambda = 10$',\
#filename u 5:1 every :::1::1 w l lw 3 lc 6 title '$\lambda = 1$',\
#filename u 5:1 every :::2::2 w l lw 3 lc 7 title '$\lambda = 0,1$'

#set ylabel ""
#set y2label "$b, c$"

#set format y ""
#set y2tics 0.2
#unset key

#plot filename u 5:3 every :::0::0 w l lw 3 lc 4 notitle '$\lambda = 10$',\
#filename u 5:3 every :::1::1 w l lw 3 lc 6 notitle '$\lambda = 1$',\
#filename u 5:3 every :::2::2 w l lw 3 lc 7 notitle '$\lambda = 0,1$'

set xrange [-0.25:21]

set ylabel "$a^* \\times 10^{-4}$"
set format y "$%g$" # \\times 10^{%T}$"
set ytics 2

plot filename u 5:($2*10000) every :::0::0 w l lw 2 lc 4 title '$\lambda = 10$',\
filename u 5:($2*10000) every :::1::1 w l lw 2 lc 6 title '$\lambda = 1$',\
filename u 5:($2*10000) every :::2::2 w l lw 2 lc 7 title '$\lambda = 0,1$'

set xrange [0:0.0055]
set xtics 0.0025

set format y ""
set y2tics 2
set format y2 "$%g$" # \\times 10^{%T}$"

set ylabel ""
unset key

plot filename u 5:($2*10000) every :::3::3 w l lw 2 lc 4 title '$\lambda = 10$',\
filename u 5:($2*10000) every :::4::4 w l lw 2 lc 6 title '$\lambda = 1$',\
filename u 5:($2*10000) every :::5::5 w l lw 2 lc 7 title '$\lambda = 0,1$'

unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
