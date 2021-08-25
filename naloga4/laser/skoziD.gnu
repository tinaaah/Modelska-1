#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf11b.tex" 

set samples 10000
set key box left width 0.1 height .3 Left reverse invert samplen 0.5
set key box opaque

filename1 = 'laser/pregled_D/p05r05.txt'
filename2 = 'laser/pregled_D/p05r1.txt' 
filename3 = 'laser/pregled_D/p05r4.txt'
filename4 = 'laser/pregled_D/p05r8.txt'
filename5 = 'laser/pregled_D/p05r16.txt'

#if (!exists("MP_LEFT"))   MP_LEFT = .15
#if (!exists("MP_RIGHT"))  MP_RIGHT = .9
#if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
#if (!exists("MP_TOP"))    MP_TOP = .9
#if (!exists("MP_GAP"))    MP_GAP = 0.05

set style line 1 lc rgb '#66c2a5' lt 1 lw 3
set style line 2 lc rgb '#fc8d62' lt 1 lw 3
set style line 3 lc rgb '#8da0cb' lt 1 lw 3
set style line 4 lc rgb '#e78ac3' lt 1 lw 3
set style line 5 lc rgb '#a6d854' lt 1 lw 3

#set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP


#set xlabel '$\tau$'
#set ylabel '$F, A$' 
#set key title '$A_0 = 0.5, \, F = 2$' left

#set logscale x

#plot filename5 u 3:2 w l ls 5 title '$r=16$',\
#filename5 u 3:1 w l ls 5 notitle '$p=0.5$$',\
#filename4 u 3:2 w l ls 4 title '$r=8$',\
#filename4 u 3:1 w l ls 4 notitle '$p=0,5$',\
#filename3 u 3:2 w l ls 3 title '$r=4$',\
#filename3 u 3:1 w l ls 3 notitle '$p=0,5$',\
#filename2 u 3:2 w l ls 2 title '$r=1$',\
#filename2 u 3:1 w l ls 2 notitle '$p=0,5$',\
#filename1 u 3:2 w l ls 1 title '$r=0.5$',\
#filename1 u 3:1 w l ls 1 notitle '$p=0,5$'

unset key
unset ytics
unset ylabel
set y2label 'fotoni'
set xlabel 'atomi'
set y2tics 7

plot filename1 u 1:2 w l ls 1 title '$r=0.5$',\
filename2 u 1:2 w l ls 2 title '$r=1$',\
filename3 u 1:2 w l ls 3 title '$r=4$',\
filename4 u 1:2 w l ls 4 title '$r=8$',\
filename5 u 1:2 w l ls 5 title '$r=16$'

#unset multiplot

#unset term
#set term dumb
#unset out
#set out '/dev/null'
