#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader size 20cm,18cm
#set out "graf9.tex"    #3 grafi za vsak plot posebej
#set out "graf12.tex"    #3 grafi za vsak plot posebej
#set out "graf13.tex"    #3 grafi za vsak plot posebej
#set out "graf14.tex"    #3 grafi za vsak plot posebej
#set out "graf15.tex"    #3 grafi za vsak plot posebej
set out "graf16.tex"    #3 grafi za vsak plot posebej

set key box top center width 1 height 0.1 Left reverse invert samplen 1
set key opaque

set size square

set xrange [0:200]
set yrange [0:200]

set samples 10000

filename1 = 'T_0.txt'
filename4 = 'T_15.txt'
filename5 = 'T_2.txt'
filename6 = 'T_225.txt'
filename7 = 'T_25.txt'
filename8 = 'T_3.txt'

set pm3d map

set autoscale fix
set palette defined (0 '#edf8b1', 1 '#2c7fb8')
set tics scale 0
unset cbtics
unset colorbox
unset key 
unset tics
unset border

#set title '{\Huge $T=0$}'
#plot filename1 matrix with image 

#set title '{\Huge $T=1.5$}'
#plot filename4 matrix with image 

#set title '{\Huge $T=2$}'
#plot filename5 matrix with image 

#set title '{\Huge $T=2.25$}' 
#plot filename6 matrix with image 

#set title '{\Huge $T=2.5$}'
#plot filename7 matrix with image 

set title '{\Huge $T=3$}'
plot filename8 matrix with image 

unset term
set term dumb
unset out
set out '/dev/null'
