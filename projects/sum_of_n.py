def func(x):
    sum = 0
    for i in range(1,x+1):
        sum = sum + i
        print(i)
    return sum
print(func(4))