# Given  names and phone numbers, assemble a phone book that maps friends'
# names to their respective phone numbers. You will then be given an
# unknown number of names to query your phone book for; for each queried,
# print the associated entry from your phone book (in the form ){Name}={Number}
# or 'Not Found' if
# there is no entry for {Name}.
import sys
t = int(raw_input())
phonebook = {}
for x in range(t):
    name, contact = raw_input().strip().split(' ')
    name, contact = [str(name), int(contact)]
    phonebook[name] = contact
for line in sys.stdin:
    name = line.strip()
    if name in phonebook:
        print ("%s=%s" % (name, phonebook[name]))
    else:
        print ("Not found")
