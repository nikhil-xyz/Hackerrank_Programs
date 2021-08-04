result = {}
result[1] = 0
result[2] = 1
result[3] = 1

for i in range(4, 1000001):
    result[i] = (result[i - 2] + result[i - 3]) % 1000000009

t = int(input())
for i in range(t):
    n = int(input())
    print(result[n])


