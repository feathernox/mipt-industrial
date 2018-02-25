RAND_STR=`head /dev/urandom | tr -dc A-Za-z0-9 | head -c 32`
echo SECRET_KEY =\'"$RAND_STR"\' > dz2/security.py
