a = int(input())
b = int(input())
c = int(input())

value = list(str(a * b * c))

for i in range(10):
    print(value.count(str(i)))
