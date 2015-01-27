#!/usr/bin/env python
"""
synopisis:

file contain records seperated by %%
count the number of %% in a file
select a random n from 1 to count
read and display the record.

"""
import sys
import random

DEBUG = 1==0

def countRecords(fn):
    if DEBUG:
        print "scanning for total number of fortunes in " + fn
    f = open(fn)
    contents = f.read()
    f.close()
    return contents.count("%%")
    

def fortuneX(fn, n):
    if DEBUG:
            print "loading fortune " + str(n)
    f = open(fn)
    contents = f.read()
    s = contents.split('%%')[n]
    return s
    


def main():
    global DEBUG
    
    if DEBUG:
            print 'Number of arguments:', len(sys.argv), 'arguments.'
            print 'Argument List:', str(sys.argv)

    ln = len(sys.argv)
    fn = "scene"
    
    if ln == 1:
        fn = "scene"
    elif ln == 2:
        if str(sys.argv[1]) == "-o":
            fn = "obscene"
        elif str(sys.argv[1])== "-d":
            DEBUG = 1==1
        else:
            fn = str(sys.argv[1])
    elif ln == 3:
        s1 = str(sys.argv[1])
        s2 = str(sys.argv[2])
        if s1 == "-o" or s2 == "-o":
            fn = "obscene"
        if s1 == "-d" or s2 == "-d":
            DEBUG = 1==1
    else:
        fn = str(sys.argv[1])
        DEBUG = 1==1
    
    
    if DEBUG:
            print "Fortune file is " + fn
    x = countRecords(fn)
    if DEBUG:
            print str(x) + " records were found"
    y = random.randint(0,x-1)
    print fortuneX(fn,y)
    

main()

