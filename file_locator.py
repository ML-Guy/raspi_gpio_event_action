#!/usr/bin/env python

import os


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)



x=find('abc.txt','/home/beyond/Downloads')
print "file found :",x
print "contents are\t"
fd=open(x,'r')
buf=fd.readline()
print buf
