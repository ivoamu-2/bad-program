import random as r
import time
def ssum(array,a,b):
        if (a != b):
            arr = array[a:b]
            return sum(arr)
        else:
            return 0
def solve(array):
    ss = 0
    for l in range(len(array)):
        for i in range(len(array)-l+1):
            s = ssum(array,l,i+l)
            if s != None:
                if s > ss:
                    ss = s
    return ss
array = []
for i in range(10):
    n = r.randint(-100,100)
    array.append(n)
a = time.time()
print(0)
sum = solve(array)
print(sum)
b = time.time()
print(b-a)
