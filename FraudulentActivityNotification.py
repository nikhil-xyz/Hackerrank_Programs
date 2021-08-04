from bisect import insort, bisect_left
import sys
n, d = map(int, input().split())
arr = list(map(int, input().split()))

temp = []
notifications = 0
for i in range(n):
    if i >= d:
        median = 0
        if (d % 2) == 0:
            median = (temp[int(d / 2) - 1] + temp[int(d / 2)]) / 2
        else:
            median = temp[int(d / 2)]

        if arr[i] >= (2 * median):
            notifications += 1
        index = bisect_left(temp, arr[i-d])
        del temp[index]

    insort(temp, arr[i])
print(notifications)
