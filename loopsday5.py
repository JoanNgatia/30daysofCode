# Given an integer,N , print its first  10 multiples. Each multiple N X i
# (where 1 < i < 10) should be printed on a new line in the form: `N x i =
# result`.

# !/bin/python

N = int(raw_input().strip())
for val in range(1, 11):
    result = N * val
    print "{} x {} = {}".format(N, val, result)
