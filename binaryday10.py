def day10(num):
    empty = []
    arr = []
    while num > 0:
        c = chr(ord('0') + int(num & 1))
        num >>= 1
        arr.append(c)
    print arr
    count = 0
    while (count < len(arr)):
        if arr[count] == 1 and arr[count + 1] != 0:
            empty.append(arr[count])
        count = count + 1
    return len(empty)
