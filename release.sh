wget --keep-session-cookies --save-cookies cookies.txt https://rsskanat.herokuapp.com/
cat cookies.txt | tail -n 1 | rev | cut -d$'\t' -f1 | rev