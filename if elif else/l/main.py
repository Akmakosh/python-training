n = int(input())
m = int(input())
k = int(input())
k != n * m

if k % n == 0 or k % m == 0:
    print('YES')
elif k >= m*n:
    print('NO')
else:
    print('NO')