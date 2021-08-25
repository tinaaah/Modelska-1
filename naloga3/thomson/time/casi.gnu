#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"

set key box top left width 1 height 0.1 Left reverse invert samplen 1
set key opaque

filename1 = 'NeldMead.txt'
filename2 = 'Powell.txt'
filename3 = 'CG.txt'
filename4 = 'BFGS.txt'

set logscale y

plot filename1 w lp pt 7 ps .7 lw 2 lc 4 title 'Nelder-Mead',\
filename2 w lp pt 7 ps .7 lw 2 lc 6 title 'Powell',\
filename3 w lp pt 7 ps .7 lw 2 lc 7 title 'CG',\
filename4 w lp pt 7 ps .7 lw 2 lc 2 title 'BFGS'

unset term
set term dumb
unset out
set out '/dev/null'