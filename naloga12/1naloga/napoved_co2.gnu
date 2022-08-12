#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf24.tex"

set key box top right width -0.5 height 0.1 Left reverse invert samplen 0.5
set key opaque

#set samples 10000
filename = 'napoved_co2.txt'

set style line 1 lt 7 lw 3 ps 1.5 lc rgb '#ef8a62'
set style line 2 lt 7 lw 3 ps 1.5 lc rgb '#67a9cf'
set style line 3 lt 7 lw 3 ps 1.5 lc rgb '#66c2a5'
set style line 4 lt 7 lw 3 ps 1.5 lc rgb '#998ec3'

set grid lc 'grey'

set ylabel '$S$'
set xlabel '$t$' 


# plot filename u 1:2 w l lc 'grey' title 'podatki',\
# filename every :::0::0 u 1:3 w l ls 2 title '$p=10$'

# plot filename u 1:2 w l lc 'grey' title 'podatki',\
# filename every :::1::1 u 1:3 w l ls 2 title '$p=20$'

# plot filename u 1:2 w l lc 'grey' title 'podatki',\
# filename every :::2::2 u 1:3 w l ls 2 title '$p=30$'


plot filename u 1:2 w l lc 'grey' title 'podatki',\
filename every :::3::3 u 1:3 w l ls 2 title '$p=40$'


unset term
set term dumb
unset out
set out '/dev/null'