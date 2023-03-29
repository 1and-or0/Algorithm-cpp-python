n = int(input())
arr = list(map(int, input().split()))

temp1 = []
temp2 = [arr[-1]]
result = 0

i = n-1-1

while i > -1:
    if arr[i] <= temp2[-1]:
        temp1.append(arr[i])

    if arr[i] > temp2[-1]:
        if len(temp1) == 0:
            temp2.append(arr[i])
        else:
            if sum(temp1) < sum(temp2):
                result += len(temp1)
                temp1 = []
                temp2.append(arr[i])
            elif sum(temp1) > sum(temp2):
                result += len(temp2)
                temp2 = temp1
                temp1 = []
                temp2.append(arr[i])

    i -= 1

print(result)
