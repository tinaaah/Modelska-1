#!/usr/bin/gnuplot
#set term epslatex colour solid rounded noheader # size 12.5cm,10cm
#set out "graf4a.tex"    #3 grafi za vsak plot posebej


set key box width 2 height 0.1 left Left reverse invert samplen 1
set key opaque

set samples 10000

filename1 = 'x_z_napako_1.txt'
filename2 = 'x_z_napako_2.txt'

#set object 1 ellipse center 1.5, 1  size 6, 12  angle 60 front fs empty bo 3
set xlabel '$t$'
set ylabel '$v_x^+ - \hat{v}_x$'

set ytics 25
set mytics 2

plot filename1 every :::0::0 u 1:($3/$3-1) w lines lc 6 lw 1 notitle '$\hat{x}$',\
filename1 every :::0::0 u 1:($3/$3+$4-1) w lines lc 4 lw 2 title '$90\%$',\
filename1 every :::1::1 u 1:($3/$3+$4-1) w lines lc 7 lw 2 title '$95\%$',\
filename1 every :::2::2 u 1:($3/$3+$4-1) w lines lc 1 lw 2 title '$99\%$',\
filename1 every :::0::0 u 1:($3/$3-$4-1) w lines lc 4 lw 2 notitle,\
filename1 every :::1::1 u 1:($3/$3-$4-1) w lines lc 7 lw 2 notitle,\
filename1 every :::2::2 u 1:($3/$3-$4-1) w lines lc 1 lw 2 notitle,\
filename1 every :::0::0 u 1:(($2-$3)-1) w lines lc 8 lw 2 title '$x^+-\hat{x}$'

#plot filename1 every :::0::0 u 1:($6/$6-1) w lines lc 6 lw 1 notitle '$\hat{v}_x$',\
#filename1 every :::0::0 u 1:($6/$6+$7-1) w lines lc 4 lw 2 title '$90\%$',\
#filename1 every :::1::1 u 1:($6/$6+$7-1) w lines lc 7 lw 2 title '$95\%$',\
#filename1 every :::2::2 u 1:($6/$6+$7-1) w lines lc 1 lw 2 title '$99\%$',\
#filename1 every :::0::0 u 1:($6/$6-$7-1) w lines lc 4 lw 2 notitle,\
#filename1 every :::1::1 u 1:($6/$6-$7-1) w lines lc 7 lw 2 notitle,\
#filename1 every :::2::2 u 1:($6/$6-$7-1) w lines lc 1 lw 2 notitle,\
#filename1 every :::0::0 u 1:(($5-$6)-1) w lines lc 8 lw 2 title '$v_x^+-\hat{v}_x$'


#unset term
#set term dumb
#unset out
#set out '/dev/null'
