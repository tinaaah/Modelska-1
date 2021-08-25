#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "el4.tex"

filename = 'thomson/powell/el4.txt'
#filename = 'thomson/nelder/el100.txt'
set parametric
set isosamples 40,40
set title '$N=4$

unset key

set tmargin at screen 0.95
set bmargin at screen 0.05
set lmargin at screen 0
set rmargin at screen 0.9

unset colorbox
unset border
unset tics

set view equal xyz
#set palette 34,35,36

R = 1.
set urange [0:pi]
set vrange [0:2*pi]
set style fill  transparent solid 0.20 border
unset hidden3d
splot R*cos(v)*sin(u),R*sin(v)*sin(u),R*cos(u) with lines lc 6,\
filename every ::1 u 1:2:3 w points lc 4 pt 7 ps 1.5

unset term
set term dumb
unset out
set out '/dev/null'
