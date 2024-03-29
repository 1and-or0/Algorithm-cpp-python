x = int(input())

d = [0] * 3001

for i in range(2, x+1):
    # 1을 더하는 경우
    d[i] = d[i-1] + 1
    # 각각 나누어 떨어질 때,
    if i % 2 == 0:  # 2를 곱한 경우 == 2로 나눈 경우
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:  # 3을 곱한 경우 == 3으로 나눈 경우
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 5 == 0:  # 5를 곱한 경우 == 5로 나눈 경우
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
