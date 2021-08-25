#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf14.tex"    #3 grafi za vsak plot posebej

set key box width 2 height 0.5 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'bin2.txt'
filename2 = 'bin4.txt'

set title '$N_0=250$'

set style fill transparent solid 0.5

plot filename1 every ::1:0::0 u ($2):($1/10000) lc 4 lw 2 smooth freq w boxes title '$\beta =1$',\
filename2  every ::1:0::0 u ($2):($1/10000) lc 6 lw 2 smooth freq w boxes title\
'$\beta_s =5 \beta, \, \beta_r=4\beta$'

unset term
set term dumb
unset out
set out '/dev/null'
