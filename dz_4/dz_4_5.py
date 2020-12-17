from functools import reduce

lis = [x for x in range(100, 1000) if x % 2 == 0 ]



def full_prozd(z, y):
    h = z * y
    return h


out_sum = reduce(full_prozd, lis)

print(out_sum)