#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf1.tex"

filename = 'powell/el3.txt'
set parametric
set isosamples 40,40
set hidden

set view equal xyz

R = 1.
set urange [0:pi]
set vrange [0:2*pi]
set style fill  transparent solid 0.20 border
unset hidden3d
splot R*cos(v)*sin(u),R*sin(v)*sin(u),R*cos(u) with lines lc 6,\
filename every ::1 u 1:2:3 w points lt 7 lc 4 ps 1
#unset term
#set term dumb
#unset out
#set out '/dev/null'
