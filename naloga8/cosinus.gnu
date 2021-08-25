#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf4.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .02
if (!exists("MP_RIGHT"))  MP_RIGHT = .995
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.1

#set multiplot layout 1,3 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP

#set samples 100000
filename = 'proba.txt'

set style fill transparent solid 0.25 
unset key

f(y) = (3*cos(y) - cos(y)**3)/4 + 0.5
h(y) = (3*y - y**3)/4 + 0.5

#set xtics 0.25
#set ytics 1
plot filename every :::0::0 using ($2):($1) smooth freq w boxes lc 4 title '$r$'

#plot filename every :::1::1 using ($2):($1) smooth freq w boxes lc 4 title '$r$',\
#h(x)



#unset term
#set term dumb
#unset out
#set out '/dev/null'
