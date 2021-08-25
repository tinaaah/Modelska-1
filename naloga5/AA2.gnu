#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf6.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,2 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename1 = 'binarna1.txt'
filename2 = 'binarna2.txt'
filename3 = 'razlika1.txt'
filename4 = 'razlika2.txt'
filename5 = 'razlika3.txt'

#plot filename1 u 5:1 every :::0::0 w lp lt 6 lc -1 title "eksaktna",\
#filename2 u 5:1 every :::0::0 w lp lt 6 lc 6 title "približek"

#set xlabel "$\\tau$"
#set yrange [-0.025:]
#set xrange [0:65]
#plot filename2 u 5:1 every :::0::0 w l lc -1 lw 3 title "$a$",\
#filename2 u 5:2 every :::0::0 w l lc 1 lw 3 title "$a^*$",\
#filename2 u 5:3 every :::0::0 w l lc 3 lw 3 title "$b=c$"

#plot filename3 u 5:(log(abs($1))) every :::0::0 w l lc -1 lw 3 title "$a$",\
#filename3 u 5:(log(abs($2))) every :::0::0 w l lc 1 lw 3 title "$a^*$",\
#filename3 u 5:(log(abs($3))) every :::0::0 w l lc 3 lw 3 title "$b=c$"

unset key
set xlabel '$log_{10} \tau$'
set xrange [-3.5:]
set xtics 1
set ylabel '$log_{10} \left|x-x_0 \right|$'

plot filename5 u (log10($5)):(log10(abs($1))) every :::0::0 w lp lc 4 lt 7 ps 0.5 title '$\lambda = 10$',\
filename5 u (log10($5)):(log10(abs($1))) every :::1::1 w lp lc 6 lt 7 ps 0.5 title '$\lambda = 1$',\
filename5 u (log10($5)):(log10(abs($1))) every :::2::2 w lp lc 7 lt 7 ps 0.5 title '$\lambda = 0,1$'

set ylabel ''
set format y ''
set format y2 '$%g$'
set y2tics 2

set key top right

plot filename5 u (log10($5)):(log10(abs($2))) every :::0::0 w lp lc 4 lt 7 ps 0.5 title '$\lambda = 10$',\
filename5 u (log10($5)):(log10(abs($2))) every :::1::1 w lp lc 6 lt 7 ps 0.5 title '$\lambda = 1$',\
filename5 u (log10($5)):(log10(abs($2))) every :::2::2 w lp lc 7 lt 7 ps 0.5 title '$\lambda = 0,1$'


#set format y ""
#set format y2 "$%g$"
#set y2tics 1
#set xtics 0.0025
#set xrange [-0.00005:0.01]
#unset yrange
#set ylabel ""

#plot filename4 u 5:(log10(abs($1))) every :::0::0 w l lc -1 lw 3 title "$a$",\
#filename4 u 5:(log10(abs($2))) every :::0::0 w l lc 1 lw 3 title "$a^*$",\
#filename4 u 5:(log10(abs($3))) every :::0::0 w l lc 3 lw 3 title "$b=c$"


unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
