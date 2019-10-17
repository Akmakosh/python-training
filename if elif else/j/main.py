y = int(input())
x = int(input())
ys = int(input())
xs = int(input())

if (ys == y+1 or ys == y-1) and (xs == x-1 or xs == x+1):
    print('YES')
elif ys == y and (xs == x+1 or xs == x-1):
    print('YES')
elif xs == x and (ys == y+1 or ys == y-1):
    print('YES')
else:
    print('NO')

