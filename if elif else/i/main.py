y = int(input())
x = int(input())
ys = int(input())
xs = int(input())

if y == xs and  x == ys or x != xs and y == ys:
    print('YES')
elif abs(y-ys) == abs(x-xs) or x == xs and y != ys:
    print('YES')
else:
    print('NO')
