#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf10.tex" #grafi predstavljajo potek populacij pri začetnem 1 zajcu in 0.25 lisice


set key box width 0.8 height .1 Left reverse invert samplen 0.5
set key box opaque

filename = 'enako.txt'

if (!exists("MP_LEFT"))   MP_LEFT = .15
if (!exists("MP_RIGHT"))  MP_RIGHT = .9
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.05


set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

#fff7ec','#fee8c8','#fdd49e','#fdbb84','#fc8d59','#ef6548','#d7301f','#b30000','#7f0000'
set style line 1 lc rgb '#ffff7f' lt 1 lw 1
set style line 2 lc rgb '#fee8c8' lt 1 lw 1
set style line 3 lc rgb '#fdd49e' lt 1 lw 1
set style line 4 lc rgb '#fdbb84' lt 1 lw 1
set style line 5 lc rgb '#fc8d59' lt 1 lw 1
set style line 6 lc rgb '#ef6548' lt 1 lw 1
set style line 7 lc rgb '#d7301f' lt 1 lw 1
set style line 8 lc rgb '#b30000' lt 1 lw 1
set style line 9 lc rgb '#7f0000' lt 1 lw 1
set style line 10 lc rgb '#a84020' lt 1 lw 1
set style line 11 lc rgb '#9e2b15' lt 1 lw 1
set style line 12 lc rgb '#95150b' lt 1 lw 1
set style line 13 lc rgb '#8b0000' lt 1 lw 1

unset key
set xlabel '$\tau$'
plot filename u 3:1 every :::0::0 w l ls 2 lw 2 notitle '$\delta = 0,2$',\
filename u 3:1 every :::1::1 w l ls 4 lw 2 notitle '$\delta = 0,15$',\
filename u 3:1 every :::2::2 w l ls 6 lw 2 notitle '$\delta = 0,1$',\
filename u 3:1 every :::3::3 w l ls 8 lw 2 notitle '$\delta = 0,05$',\
filename u 3:1 every :::4::4 w l ls 10 lw 2 notitle '$\delta = 0,025$',\
filename u 3:1 every :::5::5 w l ls 12 lw 2 notitle '$\delta = 0,0125$',\
filename u 3:2 every :::0::0 w l ls 2 lw 2 notitle '$\delta = 0,2',\
filename u 3:2 every :::1::1 w l ls 4 lw 2 notitle '$\delta = 0,15',\
filename u 3:2 every :::2::2 w l ls 6 lw 2 notitle '$\delta = 0,1',\
filename u 3:2 every :::3::3 w l ls 8 lw 2 notitle '$\delta = 0,05',\
filename u 3:2 every :::4::4 w l ls 10 lw 2 notitle '$\delta = 0,025',\
filename u 3:2 every :::5::5 w l ls 12 lw 2 notitle '$\delta = 0,0125',\


unset key 
set ylabel ""
set format y ""
set y2label "fotoni"
set xlabel "atomi"
set format y2 "%g"
set y2tics 0.05
set xtics 0.2
plot filename u 1:2 every :::0::0 w l ls 2 lw 2 notitle '$\Delta = 0,2$',\
filename u 1:2 every :::1::1 w l ls 4 lw 2 notitle '$\Delta = 0,15$',\
filename u 1:2 every :::2::2 w l ls 6 lw 2 notitle '$\Delta = 0,1$',\
filename u 1:2 every :::3::3 w l ls 8 lw 2 notitle '$\Delta = 0,05$',\
filename u 1:2 every :::4::4 w l ls 10 lw 2 notitle '$\Delta = 0,025$',\
filename u 1:2 every :::5::5 w l ls 12 lw 2 notitle '$\Delta = 0,0125$'



unset term
set term dumb
unset out
set out '/dev/null'
