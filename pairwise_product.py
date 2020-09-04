# Uses python3


def MaxPairwiseProductFast(n, a):
    max_index1 = -1
    for i in range(0, n):
        if a[i] > a[max_index1]:
            max_index1 = i
        else:
            continue
    # the value of the other index should be different compared to the        #first, else it will assume the same indices for both the max
    max_index2 = -2
    for j in range(0, n):
        if a[j] > a[max_index2] and a[j] != a[max_index1]:
            max_index2 = j
        else:
            continue

    Product2 = a[max_index1]*a[max_index2]
    return Product2


n = int(input())
a = [int(x) for x in input().split()]
c = list()

print(MaxPairwiseProductFast(n, a))
