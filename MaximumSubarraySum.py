from bisect import bisect, insort
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    temp = []
    current_sum = 0
    result = 0
    for j in range(n):
        current_sum = (arr[j] + current_sum) % m
        index = bisect(temp, current_sum)

        d = 0 if index == j else temp[index]
        result = max(result, (current_sum - d + m) % m)
        insort(temp, current_sum)

    print(result)


