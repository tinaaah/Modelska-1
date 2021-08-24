#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf4.tex"

set key box left width 4 height .1 Left reverse invert samplen 1

set ylabel '$u(\tau, u_0, c)$'
set xlabel '$\tau$'

u0=0.5

c1=0.001
c2=1.
c3=10.
c4=50.

uc1=(1-u0)*1/(1-tanh(sqrt(c1))/(sqrt(c1)))
uc2=(1-u0)*1/(1-tanh(sqrt(c2))/(sqrt(c2)))
uc3=(1-u0)*1/(1-tanh(sqrt(c3))/(sqrt(c3)))
uc4=(1-u0)*1/(1-tanh(sqrt(c4))/(sqrt(c4)))

f1(x) = (u0-uc1)*(cosh(sqrt(c1)*x) - tanh(sqrt(c1))*sinh(sqrt(c1)*x)) + uc1
f2(x) = (u0-uc2)*(cosh(sqrt(c2)*x) - tanh(sqrt(c2))*sinh(sqrt(c2)*x)) + uc2
f3(x) = (u0-uc3)*(cosh(sqrt(c3)*x) - tanh(sqrt(c3))*sinh(sqrt(c3)*x)) + uc3
f4(x) = (u0-uc4)*(cosh(sqrt(c4)*x) - tanh(sqrt(c4))*sinh(sqrt(c4)*x)) + uc4

set xrange [0:1]
set yrange [0:]

plot f1(x) w lines lw 2 title '$c=0,001$',\
f2(x) w lines lw 2 title '$c=1$',\
f3(x) w lines lw 2 title '$c=10$',\
f4(x) w lines lw 2 title '$c=50$'

unset term
set term dumb
unset out
set out '/dev/null'
