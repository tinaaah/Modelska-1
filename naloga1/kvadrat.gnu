#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"

set key box left width 4 height .1 Left reverse invert samplen 1

set ylabel '$u(\tau, u_0)$'
set xlabel '$\tau$'

f1(x) = -3/2 * (1-u1) * x**2 + 3 * (1-u1) * x + u1
f2(x) = -3/2 * (1-u2) * x**2 + 3 * (1-u2) * x + u2
f3(x) = -3/2 * (1-u3) * x**2 + 3 * (1-u3) * x + u3
f4(x) = -3/2 * (1-u4) * x**2 + 3 * (1-u4) * x + u4
f5(x) = -3/2 * (1-u5) * x**2 + 3 * (1-u5) * x + u5

set xrange [0:1]
set yrange [0:]

u1=0
u2=0.5
u3=1
u4=1.5
u5=2

set style fill transparent solid 0.1 border

plot f1(x) w filledcurves y=0 title '$u_0=0$',\
f2(x) w filledcurves y=0 title '$u_0=0,5$',\
f3(x) w filledcurves y=0 title '$u_0=1$',\
f4(x) w filledcurves y=0 title '$u_0=1,5$',\
f5(x) w filledcurves y=0 title '$u_0=2$'

unset term
set term dumb
unset out
set out '/dev/null'
