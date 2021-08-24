set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf2.tex"

set key box left width 6 height .1 Left reverse invert samplen 1

set ylabel '$u(\tau,u_0,p)$'
set xlabel '$\tau$'

f1(x) = (4*P1-1)/(2*P1) * (1 - u1) * (1 - (1-x)**(2*P1/(2*P1-1))) + u1
f2(x) = (4*P2-1)/(2*P2) * (1 - u2) * (1 - (1-x)**(2*P2/(2*P2-1))) + u2
f3(x) = (4*P3-1)/(2*P3) * (1 - u3) * (1 - (1-x)**(2*P3/(2*P3-1))) + u3
f4(x) = (4*P4-1)/(2*P4) * (1 - u4) * (1 - (1-x)**(2*P4/(2*P4-1))) + u4

set xrange [0:1]

u1=0.5 
u2=0.5 
u3=0.5 
u4=0.5 

P1=-10.
P2=-1.
P3=1.
P4=10.

set style fill transparent solid 0.2 border

plot f1(x) w filledcurves y=0 title '$u_0=0,5, p=-10$',\
f2(x) w filledcurves y=0 title '$u_0=0,5, p=-1$',\
f4(x) w filledcurves y=0 title '$u_0=0,5, p=10$',\
f3(x) w filledcurves y=0 title '$u_0=0,5, p=1$'
  

unset term
set term dumb
unset out
set out '/dev/null'
