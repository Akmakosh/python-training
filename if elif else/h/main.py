y = int(input())
x = int(input())
ys = int(input())
xs = int(input())

if y == xs and  x == ys :
    print('YES')
elif abs(y-ys) == abs(x-xs):
    print('YES')
else:
    print('NO')
