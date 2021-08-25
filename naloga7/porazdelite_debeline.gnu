#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf8.tex"    #3 grafi za vsak plot posebej

set key box width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'sipanja_v_steni.txt'

set style fill transparent solid 0.25 
set xrange [0:40]

plot filename every :::0::0 using ($2):($1/10000) lc 1 smooth freq w boxes title '$\alpha=0,1$',\
filename every :::1::1 using ($2):($1/10000) lc 7 smooth freq w boxes title '$\alpha = 0,25$' ,\
filename every :::2::2 using ($2):($1/10000) lc 4 smooth freq w boxes title '$\alpha = 0,5$' ,\
filename every :::3::3 using ($2):($1/10000) lc 5 smooth freq w boxes title '$\alpha = 0,75$',\
filename every :::4::4 using ($2):($1/10000) lc 3 smooth freq w boxes title '$\alpha = 1$' 

unset term
set term dumb
unset out
set out '/dev/null'
