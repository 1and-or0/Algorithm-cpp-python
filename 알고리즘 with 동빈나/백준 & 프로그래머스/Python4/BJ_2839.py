total = int(input())

nums_of_5 = total // 5
nums_of_3 = (total - nums_of_5*5) // 3

rest_ = total - nums_of_5*5 - nums_of_3*3

is_exist = True
while rest_ != 0:
    if nums_of_5 > 0:
        nums_of_5 -= 1
    else: # nums_of_3 > 0:
        is_exist = False
        break

    nums_of_3 = (total - nums_of_5*5) // 3
    rest_ = total - nums_of_5*5 - nums_of_3*3


if is_exist:
    print(nums_of_5 + nums_of_3)
else:
    print(-1)
