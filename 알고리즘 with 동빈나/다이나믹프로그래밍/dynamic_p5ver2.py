n = int(input())
arr = list(map(int, input().split()))

result = 0
temp = arr[0]
removed = []
for i in range(1, n):

    if temp >= arr[i]:
        removed.append(arr[i])
    elif temp < arr[i]:
        temp = arr[i]
        if len(removed) != 0:
            result += len(removed)


print(result)
