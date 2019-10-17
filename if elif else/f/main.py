x = int(input())
y = int(input())
n = int(input())

if x >= y and x >= n:
    print(x)
elif y >= x and y >= n:
    print(y)
else:
    print(n)