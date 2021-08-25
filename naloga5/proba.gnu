#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf1.tex" 

set key box width 2 height 0.5 reverse samplen 1
set key opaque

filename = 'temp.txt'

#plot filename u (log10($5)):(log10($1)) w l lw 2 title '$x$',\
#filename u (log10($5)):(log10($2)) w l lw 2 title '$y$',\
#filename u (log10($5)):(log10($3)) w l lw 2 title '$z$',\
#filename u (log10($5)):(log10($4)) w l lw 2 title '$w$'

plot filename u 5:1 w l lc 7 lw 2 title '$x$',\
filename u 5:2 w l lc 4 lw 2 title '$y$',\
filename u 5:3 w l lc 6 lw 2 title '$z$'
#filename u 5:4 w l lw 2 title '$w$'


#plot filename u (log10($4)):1 w l lc 7 lw 2 title '$x$',\
#filename u (log10($4)):2 w l lc 4 lw 2 title '$y$',\
#filename u (log10($4)):3 w l lc 6 lw 2 title '$z$',\
#filename u (log10($4)):($1+$2+$3) w l lc -1 lw 2 title '$A$'



#unset term
#set term dumb
#unset out
#set out '/dev/null'
