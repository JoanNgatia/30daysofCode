#!/bin/python
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

N = int(raw_input().strip())
if N % 2 != 0:
    print 'Weird'
else:
    if N > 1 and N < 6:
        print 'Not Weird'
    elif N > 7 and N < 21:
        print 'Weird'
    else:
        print 'Not Weird'
