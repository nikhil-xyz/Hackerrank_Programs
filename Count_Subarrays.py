t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    count = 0
    j = 1
    elements = 0
    while j < n:
        temp = 1
        k = j
        while arr[k] >= arr[k-1]:
            k += 1
            temp += 1
            if k == n:
                break

        if k > j:
            j = k
            count += temp * (temp + 1) / 2
            elements += temp
        else:
            j += 1

    count += (n - elements)
    print(int(count))
