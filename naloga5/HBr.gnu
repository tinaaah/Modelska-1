#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf10.tex" 

set key box width 0.8 height 0.5 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

#set multiplot layout 1,3 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

filename0 = 'kislina0.txt'
filename1 = 'kislina1.txt'

set xlabel '$\log_{10}\tau$'

#plot filename0 u 4:1 w l lc 7 lw 3 title '$x$',\
#filename0 u 4:2 w l lc 4 lw 3 title '$y$',\
#filename0 u 4:3 w l lc 6 lw 3 title '$z$',\
#filename0 u 4:($1+$2+$3) w l lc -1 lw 3 title '$A$'

#plot filename1 u (log10($4)):(log10($1)) every :::2::2 w l lc 7 lw 2 title '$x$',\
#filename1 u (log10($4)):(log10($2)) every :::2::2 w l lc 4 lw 2 title '$y$',\
#filename1 u (log10($4)):(log10($3)) every :::2::2 w l lc 6 lw 2 title '$z$'

#set key bottom right
#plot filename1 u (log10($4)):(log10($1)) every :::0::0 w l lc 7 lw 3 title '$\kappa = 100$',\
#filename1 u (log10($4)):(log10($1)) every :::1::1 w l lc 4 lw 3 title '$\kappa = 10$',\
#filename1 u (log10($4)):(log10($1)) every :::2::2 w l lc 2 lw 3 title '$\kappa = 1$',\
#filename1 u (log10($4)):(log10($1)) every :::3::3 w l lc 6 lw 3 title '$\kappa = 0,1$',\
#filename1 u (log10($4)):(log10($1)) every :::4::4 w l lc 1 lw 3 title '$\kappa = 0,01$'

#unset key
#set format y ""
#plot filename1 u (log10($4)):(log10($2)) every :::0::0 w l lc 7 lw 2 title '$\kappa = 100$',\
#filename1 u (log10($4)):(log10($2)) every :::1::1 w l lc 4 lw 2 title '$\kappa = 10$',\
#filename1 u (log10($4)):(log10($2)) every :::2::2 w l lc 2 lw 2 title '$\kappa = 1$',\
#filename1 u (log10($4)):(log10($2)) every :::3::3 w l lc 6 lw 2 title '$\kappa = 0,1$',\
#filename1 u (log10($4)):(log10($2)) every :::4::4 w l lc 1 lw 2 title '$\kappa = 0,01$'

#unset key
#set format y2 "$%g$"
#set y2tics 0.5
#plot filename1 u (log10($4)):(log10($3)) every :::0::0 w l lc 7 lw 2 title '$\kappa = 100$',\
#filename1 u (log10($4)):(log10($3)) every :::1::1 w l lc 4 lw 2 title '$\kappa = 10$',\
#filename1 u (log10($4)):(log10($3)) every :::2::2 w l lc 2 lw 2 title '$\kappa = 1$',\
#filename1 u (log10($4)):(log10($3)) every :::3::3 w l lc 6 lw 2 title '$\kappa = 0,1$',\
#filename1 u (log10($4)):(log10($3)) every :::4::4 w l lc 1 lw 2 title '$\kappa = 0,01$'



#plot filename1 u 4:($2/$3) every :::0::0 w l lw 2 title '$\kappa = 100$',\
#filename1 u 4:($2/$3) every :::1::1 w l lw 2 title '$\kappa = 1$',\
#filename1 u 4:($2/$3) every :::2::2 w l lw 2 title '$\kappa = 0,01$'

unset multiplot

#unset term
#set term dumb
#unset out
#set out '/dev/null'
