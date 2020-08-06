# MAXIMUM PAIRWISE PROduct
n = int(input())
x = [int(a) for a in input().split()]


def maximum1(x):
    length = len(x)//2
    for i in range(0, length):
        for j in range(n-1, length-1):
            if x[i] > x[j]:
                max1 = x[i]
                return max1


max1 = int(maximum1(x))


def maximum2(x):
    length = len(x)//2
    for i in range(0, length):
        if x[i] != max1:
            for j in range(n-1, length-1):
                if x[j] != max1:
                    if x[i] > x[j]:
                        max2 = x[i]
                        return max2


max2 = int(maximum2(x))
print(max1*max2)
