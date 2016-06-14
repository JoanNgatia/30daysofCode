# Given an array, , of  integers,
# print 's elements in reverse order as a
# single line of space-separated numbers.

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
for val in arr[::-1]:
    print val,
