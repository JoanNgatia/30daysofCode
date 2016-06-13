# Enter your code here. Read input from STDIN. Print output to STDOUT
# name = str(raw_input())
# even_indexed = []
# odd_indexed = []
# length = len(name)
# for val in range(0, length):
# if val % 2 == 0:
#     even_indexed.append(name[val])
#  else:
#       odd_indexed.append(name[val])
# print even_indexed, odd_indexed

T = int(raw_input())

for i in range(0, T):
    S = raw_input()
    print S[::2],
    print S[1::2]
