#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf1.tex"

filename = 'bolanirazredi.txt'

plot filename u 9:1 w l lw 1.5 title 'dovzetni',\
filename u 9:2 w l lw 1.5 title '1. bolezen',\
filename u 9:3 w l lw 1.5 title '2. bolezen',\
filename u 9:4 w l lw 1.5 title '3. bolezen',\
filename u 9:5 w l lw 1.5 title '4. bolezen',\
filename u 9:6 w l lw 1.5 title '5. bolezen',\
filename u 9:7 w l lw 1.5 title '6. bolezen',\
filename u 9:8 w l lw 1.5 title 'imuni'

#plot filename u 1:2 w l title 'krožnica'

#unset term
#set term dumb
#unset out
#set out '/dev/null'
