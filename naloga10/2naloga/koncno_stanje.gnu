#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf17.tex"    #3 grafi za vsak plot posebej
#set out "graf18.tex"    #3 grafi za vsak plot posebej
#set out "graf19.tex"    #3 grafi za vsak plot posebej
#set out "graf20.tex"    #3 grafi za vsak plot posebej
#set out "graf21.tex"    #3 grafi za vsak plot posebej
set out "graf22.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set size square

set xrange [0:200]
set yrange [0:200]

set samples 10000

filename1 = 't_0.txt'
filename4 = 't_15.txt'
filename5 = 't_2.txt'
filename6 = 't_225.txt'
filename7 = 't_25.txt'
filename8 = 't_3.txt'

set pm3d map

set autoscale fix
set palette defined (0 '#edf8b1', 1 '#2c7fb8')
set tics scale 0
unset cbtics
unset colorbox
unset key 
unset tics
unset border

#set title '$T=0$'
#plot filename1 matrix with image 

#set title '$T=1.5$'
#plot filename4 matrix with image 

#set title '$T=2$'
#plot filename5 matrix with image 

#set title '$T=2.25$'
#plot filename6 matrix with image 

#set title '$T=2.5$'
#plot filename7 matrix with image 

set title '$T=3$'
plot filename8 matrix with image 

unset term
set term dumb
unset out
set out '/dev/null'
