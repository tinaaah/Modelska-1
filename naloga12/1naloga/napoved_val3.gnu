#!/usr/bin/gnuplot
set term epslatex colour solid rounded noheader
set out "graf17.tex"

set key box top right width -0.5 height 0.1 Left reverse invert samplen 0.5
set key opaque

#set samples 10000
filename1 = 'napoved_val3.txt'

set style line 1 lt 7 lw 3 ps .5 lc rgb '#d53e4f'
set style line 2 lt 7 lw 3 ps .5 lc rgb '#fc8d59'
set style line 3 lt 7 lw 3 ps .5 lc rgb '#fee08b'
set style line 4 lt 7 lw 3 ps .5 lc rgb '#99d594'
set style line 5 lt 7 lw 3 ps .5 lc rgb '#3288bd'
set style line 6 lt 7 lw 3 ps .5 lc rgb '#998ec3'

#set style fill transparent solid 0.5

set ylabel '$S_n$'
set xlabel '$n$' 
set xrange [:512]

# plot filename1 every :::0::0 u 0:1 w l ls 1 lc 'grey' title 'podatki',\
# filename1 every :::0::0 u 0:2 w l ls 1 title 'napoved $p=5$'

# plot filename1 every :::0::0 u 0:1 w l ls 1 lc 'grey' title 'podatki',\
# filename1 every :::2::2 u 0:2 w l ls 2 title "napoved $p=5$ - popravljena"

# plot filename1 every :::0::0 u 0:1 w l ls 1 lc 'grey' title 'podatki',\
# filename1 every :::1::1 u 0:2 w l ls 5 title "napoved $p=15$"

plot filename1 every :::0::0 u 0:1 w l ls 1 lc 'grey' title 'podatki',\
filename1 every :::3::3 u 0:2 w l ls 6 title "napoved $p=15$ - popravljena"

unset term
set term dumb
unset out
set out '/dev/null'