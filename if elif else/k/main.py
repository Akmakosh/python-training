y = int(input())
x = int(input())
ys = int(input())
xs = int(input())

if (ys == y+2 or ys == y-2) and( xs == x+1 or xs == x-1):
    print('YES')
elif (ys == y-1 or ys == y+1)  and (xs == x+2 or xs == x-2) :
    print('YES')
else:
    print('NO')
