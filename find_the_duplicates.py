#!/usr/bin/env python
import hashlib, os

d = dict()

for file in os.listdir("/home/bharati/python_code"):
    if file.endswith(".dat"):
        chk = (hashlib.md5(open(file,'rb').read()).hexdigest())
        value = file
        if chk in d.keys():
            d[chk].append(value)
        else:
            d[chk] = [value]

for key, val in d.items():
    print (key, val, len(filter(bool,val)))
