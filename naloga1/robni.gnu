#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf3.tex"

set key box left width 4 height .1 Left reverse invert samplen 1

set ylabel '$u(\tau, u_1)$'
set xlabel '$\tau$'

f1(x) = -6 * (1- (u1+u0)/2 ) * x**2 + 2 * (3-u1-2*u0) * x + u0
f2(x) = -6 * (1- (u2+u0)/2 ) * x**2 + 2 * (3-u2-2*u0) * x + u0
f3(x) = -6 * (1- (u3+u0)/2 ) * x**2 + 2 * (3-u3-2*u0) * x + u0
f4(x) = -6 * (1- (u4+u0)/2 ) * x**2 + 2 * (3-u4-2*u0) * x + u0
f5(x) = -6 * (1- (u5+u0)/2 ) * x**2 + 2 * (3-u5-2*u0) * x + u0

set xrange [0:1]
set yrange [0:]

u0=0.5
u1=0
u2=0.5
u3=1
u4=1.5
u5=2

set style fill transparent solid 0.1 border

plot f1(x) w filledcurves y=0 title '$u_1=0$',\
f2(x) w filledcurves y=0 title '$u_1=0,5$',\
f3(x) w filledcurves y=0 title '$u_1=1$',\
f4(x) w filledcurves y=0 title '$u_1=1,5$',\
f5(x) w filledcurves y=0 title '$u_1=2$'

unset term
set term dumb
unset out
set out '/dev/null'
