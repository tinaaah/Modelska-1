#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader  #size 12.5cm,10cm
set out "graf7.tex" #grafi predstavljajo potek populacij pri začetnem 1 zajcu in 0.25 lisice


filename = 'casi.txt'

f(x) = 2*pi
set ylabel '$\omega$'
set xlabel '$z_0$'
set xrange [0.5:1.01]
set yrange [0:]
set ytics 4

#set label '$\omega = 2\pi$' at 0.55, 6.5 front
set ytics add ('$2\pi$' 2*pi)

plot filename u 2:1 w linespoints lc -1 lw 2 pt 7 notitle,\
f(x) w line dt 2 lw 2 lc 4 notitle


unset term
set term dumb
unset out
set out '/dev/null'
