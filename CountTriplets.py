n, r = map(int, input().split())
arr = list(map(int, input().split()))
count1 = {}
count2 = {}
count = 0
for i in arr:
    if i in count2:
        count += count2[i]
    if i in count1:
        if (i*r) not in count2:
            count2[i*r] = count1[i]
        else:
            count2[i*r] += count1[i]

        if (i*r) not in count1:
            count1[i*r] = 0
        count1[i*r] += 1

    elif (i*r) in count1:
        count1[i*r] += 1
    else:
        count1[i*r] = 1
print(count)