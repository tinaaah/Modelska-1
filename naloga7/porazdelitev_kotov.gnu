#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf9b.tex"    #3 grafi za vsak plot posebej

set key box top right width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename1 = 'plosca/prepustnost_fi.txt'
filename2 = 'plosca/prepustnost_th.txt'
filename3 = 'plosca/reflektivnost_fi.txt'
filename4 = 'plosca/reflektivnost_th.txt'

set style fill transparent solid 0.25

#set xrange [-pi/16:33*pi/16]
set xrange [-pi/32:33*pi/32]
#set xlabel '$\phi$'
set xlabel '$\theta$'

set xtics ('$0$' 0, '$\pi/4$' pi/4, '$\pi/2$' pi/2, '$3\pi/4$' 3*pi/4, '$\pi$' pi)
#set xtics ('$0$' 0, '$\pi/4$' pi/4, '$\pi/2$' pi/2, '$3\pi/4$' 3*pi/4, '$\pi$' pi,\
#'$5\pi/4$' 5*pi/4, '$3\pi/2$' 3*pi/2, '$7\pi/4$' 7*pi/4, '$2\pi$' 2*pi)

#plot filename3 every :::0::0 using ($2):($1/100000) lc 1 smooth freq w boxes title '$\alpha=0,1$',\
#filename3 every :::1::1 using ($2):($1/100000) lc 7 smooth freq w boxes title '$\alpha = 0,25$' ,\
#filename3 every :::2::2 using ($2):($1/100000) lc 4 smooth freq w boxes title '$\alpha = 0,5$' ,\
#filename3 every :::3::3 using ($2):($1/100000) lc 5 smooth freq w boxes title '$\alpha = 0,75$',\
#filename3 every :::4::4 using ($2):($1/100000) lc 3 smooth freq w boxes title '$\alpha = 1$' 

plot filename2 every :::4::4 using ($2):($1/100000) lc 3 smooth freq w boxes title '$\alpha = 1$' ,\
filename2 every :::3::3 using ($2):($1/100000) lc 5 smooth freq w boxes title '$\alpha = 0,75$',\
filename2 every :::2::2 using ($2):($1/100000) lc 4 smooth freq w boxes title '$\alpha = 0,5$' ,\
filename2 every :::1::1 using ($2):($1/100000) lc 7 smooth freq w boxes title '$\alpha = 0,25$' ,\
filename2 every :::0::0 using ($2):($1/100000) lc 9 smooth freq w boxes title '$\alpha=0,1$'

#unset term
#set term dumb
#unset out
#set out '/dev/null'
