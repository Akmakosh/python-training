n = int(input())
s = 0

for i in range (n):
    x = int(input())
    if x == 0:
        s+=1

if s > 0:
    print('YES')
else:
    print('NO')