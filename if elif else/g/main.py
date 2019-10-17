x = int(input())
y = int(input())
xs = int(input())
ys = int(input())

if x != xs and y == ys:
    print('YES')
elif x == xs and y != ys:
    print('YES')
else:
    print('NO')
