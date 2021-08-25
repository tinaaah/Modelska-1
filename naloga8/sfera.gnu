#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf4.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .02
if (!exists("MP_RIGHT"))  MP_RIGHT = .995
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.1

set multiplot layout 1,3 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

set samples 10000
filename = 'krogla.txt'

set style fill transparent solid 0.25 
unset key

set title '$r$'
set xtics 0.25
set ytics 1
plot filename every :::0::0 using ($2):($1) smooth freq w boxes lc -1 title '$r$',\

set title '$\varphi$'
set ytics 0.05
set xtics (0, '$\pi$' pi, '$2\pi$' 2*pi)
set xrange [-0.05:2*pi+0.05] 
plot filename every :::1::1 using ($2):($1) smooth freq w boxes lc -1 title '$\varphi$'

set ytics 0.1
set title '$\vartheta$'
set xtics (0, '$\pi$' pi)
set xrange [-0.05:pi+0.05] 
plot filename every :::2::2 using ($2):($1) smooth freq w boxes lc -1 title '$\vartheta$'

unset multiplot 

unset term
set term dumb
unset out
set out '/dev/null'
