#!/usr/bin/gnuplot
set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf6.tex"

#set key box right width 3 height .1 Left reverse invert samplen 1
set samples 1000

set multiplot layout 2,2

u0=0.5
T=2
L=1

set xrange [0:1+L]
set yrange [0:]

lambda1 = 6*(2*T**2 - (2*T**2 - T - 1)*u0 - 3*L + 2*T - 4)/(4*T**2 - 5*T + 1)
lambda2 = 6*((T - 1)*u0 + 2*L - 3*T + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

A1=6*(2*T**2 - 2*(T**2 - T)*u0 - L - T - 1)/(4*T**2 - 5*T + 1)
A2=6*((2*L + 3)*T - 3*T**2 + (T**2 - T)*u0)/(4*T**3 - 9*T**2 + 6*T - 1)
B1=u0
B2=(6*T**3 - 9*(L + 1)*T - (2*T**3 - 3*T + 1)*u0 + 3*L + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

u1(x) = (x>=0 && x<=1) ? -lambda1/2*x**2 + A1*x +B1 : 1/0
u2(x) = (x>=1 && x<=1+L) ? -lambda2/2*x**2 + A2*x +B2 : 1/0

set ytics 0.4

set lmargin 6
set rmargin 2
set bmargin 2
set tmargin 1

set xlabel ''
set ylabel '$u(\tau)$' offset 1
 
plot u1(x) lc 6 lw 2 notitle '$u1(\tau)$',\
u2(x) lc 4 lw 2 notitle '$u2(\tau)$'

u0=0.5
T=4
L=1

set xrange [0:1+L]
set yrange [0:]

lambda1 = 6*(2*T**2 - (2*T**2 - T - 1)*u0 - 3*L + 2*T - 4)/(4*T**2 - 5*T + 1)
lambda2 = 6*((T - 1)*u0 + 2*L - 3*T + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

A1=6*(2*T**2 - 2*(T**2 - T)*u0 - L - T - 1)/(4*T**2 - 5*T + 1)
A2=6*((2*L + 3)*T - 3*T**2 + (T**2 - T)*u0)/(4*T**3 - 9*T**2 + 6*T - 1)
B1=u0
B2=(6*T**3 - 9*(L + 1)*T - (2*T**3 - 3*T + 1)*u0 + 3*L + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

u1(x) = (x>=0 && x<=1) ? -lambda1/2*x**2 + A1*x +B1 : 1/0
u2(x) = (x>=1 && x<=1+L) ? -lambda2/2*x**2 + A2*x +B2 : 1/0

set lmargin 4
set rmargin 4
set bmargin 2
set tmargin 1

set ylabel ''

plot u1(x) lc 6 lw 2 notitle '$u1(\tau)$',\
u2(x) lc 4 lw 2 notitle '$u2(\tau)$'

u0=0.5
T=2
L=4


set xrange [0:1+L]
set yrange [0:]

lambda1 = 6*(2*T**2 - (2*T**2 - T - 1)*u0 - 3*L + 2*T - 4)/(4*T**2 - 5*T + 1)
lambda2 = 6*((T - 1)*u0 + 2*L - 3*T + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

A1=6*(2*T**2 - 2*(T**2 - T)*u0 - L - T - 1)/(4*T**2 - 5*T + 1)
A2=6*((2*L + 3)*T - 3*T**2 + (T**2 - T)*u0)/(4*T**3 - 9*T**2 + 6*T - 1)
B1=u0
B2=(6*T**3 - 9*(L + 1)*T - (2*T**3 - 3*T + 1)*u0 + 3*L + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

u1(x) = (x>=0 && x<=1) ? -lambda1/2*x**2 + A1*x +B1 : 1/0
u2(x) = (x>=1 && x<=1+L) ? -lambda2/2*x**2 + A2*x +B2 : 1/0

set xlabel '$\tau$'
set ylabel '$u(\tau)$'

set lmargin 6
set rmargin 2
set bmargin 3
set tmargin 0

set ytics 1.5
plot u1(x) lc 6 lw 2 notitle '$u1(\tau)$',\
u2(x) lc 4 lw 2 notitle '$u2(\tau)$'

u0=0.5
T=4
L=4

set xrange [0:1+L]
set yrange [0:]

lambda1 = 6*(2*T**2 - (2*T**2 - T - 1)*u0 - 3*L + 2*T - 4)/(4*T**2 - 5*T + 1)
lambda2 = 6*((T - 1)*u0 + 2*L - 3*T + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

A1=6*(2*T**2 - 2*(T**2 - T)*u0 - L - T - 1)/(4*T**2 - 5*T + 1)
A2=6*((2*L + 3)*T - 3*T**2 + (T**2 - T)*u0)/(4*T**3 - 9*T**2 + 6*T - 1)
B1=u0
B2=(6*T**3 - 9*(L + 1)*T - (2*T**3 - 3*T + 1)*u0 + 3*L + 3)/(4*T**3 - 9*T**2 + 6*T - 1)

u1(x) = (x>=0 && x<=1) ? -lambda1/2*x**2 + A1*x +B1 : 1/0
u2(x) = (x>=1 && x<=1+L) ? -lambda2/2*x**2 + A2*x +B2 : 1/0

set lmargin 4
set rmargin 4
set bmargin 3
set tmargin 0

set ylabel ''
set ytics 0.4
plot u1(x) lc 6 lw 2 notitle '$u1(\tau)$',\
u2(x) lc 4 lw 2 notitle '$u2(\tau)$'

#f5(x) w filledcurves y=0 title '$u_0=2$'

unset term
set term dumb
unset out
set out '/dev/null'
