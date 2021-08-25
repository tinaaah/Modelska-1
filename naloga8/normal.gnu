#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf3.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

if (!exists("MP_LEFT"))   MP_LEFT = .05
if (!exists("MP_RIGHT"))  MP_RIGHT = .95
if (!exists("MP_BOTTOM")) MP_BOTTOM = .1
if (!exists("MP_TOP"))    MP_TOP = .9
if (!exists("MP_GAP"))    MP_GAP = 0.02

set multiplot layout 1,3 columnsfirst margins screen MP_LEFT, MP_RIGHT, MP_BOTTOM, MP_TOP spacing screen MP_GAP


set samples 100000
filename = 'primerjava.txt'

mu = 0
sigma = 1
g(x) = 1/(sqrt(2*pi)*sigma) * exp( -(x-mu)**2/(2*sigma**2))

set style fill transparent solid 0.25 

set title '$N=100$'
set yrange [0:0.5]
set xrange [-3.5:3.5]
set xtics 1
unset key

plot filename every :::0::0 using ($3):($1) lc 3 smooth freq w boxes title 'Konvolucija',\
filename every :::1::1 using ($3):($1) lc 7 smooth freq w boxes title 'Box-Muller',\
g(x) lc -1 title 'Gauss'

set ytics format ''
set title '$N=1000$'

plot filename every :::2::2 using ($3):($1) lc 3 smooth freq w boxes title '$\text{Konvolucija}$',\
filename every :::3::3 using ($3):($1) lc 7 smooth freq w boxes title '$\text{Box-Muller}$',\
g(x) lc -1 title 'Gauss'

set key
set title '$N=10000$'
plot filename every :::4::4 using ($3):($1) lc 3 smooth freq w boxes title 'Konvolucija',\
filename every :::5::5 using ($3):($1) lc 7 smooth freq w boxes title 'Box-Muller',\
g(x) lc -1 title 'Gauss'

unset multiplot

unset term
set term dumb
unset out
set out '/dev/null'
