#!/usr/bin/gnuplot
#set term cairolatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf5.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 Left reverse invert samplen 1
set key opaque

set samples 10000
filename = 'inovacija.txt'

stats filename every :::1::1 name 'A'
stats filename every :::0::0 name 'B'

#set style fill transparent solid 0.25 
set label '$\mu_A$' at 1250,40 front
set label '$\mu_B$' at 1250,35 front

plot filename every :::0::0 lc 2 w l title '$B=$ vsaka $5./10.$ meritev',\
filename every :::1::1 lc 7 w l title '$A=$ vsaka meritev',\
B_mean_y lc 8 lw 2 notitle,\
A_mean_y lc 8 lw 2 notitle


#unset term
#set term dumb
#unset out
#set out '/dev/null'
