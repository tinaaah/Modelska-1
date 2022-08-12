#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
set out "graf1.tex"    ## Funkciji 
#set out "graf2.tex"    ## Odvod funkcij

set key box left width 2 height 0.2 Left reverse invert samplen 1
set key opaque

set samples 10000

set grid lc 'dark-gray' dt 2


f(x) = tanh(x)
F(x) = 1 - f(x)**2
g(x) = 1/(1+exp(-x))
G(x) = g(x)*(1-g(x))

set xrange [-5:5]
set yrange [-1:1]

plot f(x) lc '#8da0cb' lw 3 title '$\tanh(x)$',\
g(x) lc '#fc8d62' lw 3 title '$\sigma(x)$'

#set xrange [-5:5]
#set yrange [0:1]

#plot F(x) lc '#8da0cb' lw 3 title '$\tanh^{,}(x)$',\
#G(x) lc '#fc8d62' lw 3 title '$\sigma^{,}(x)$'

unset term
set term dumb
unset out
set out '/dev/null'
