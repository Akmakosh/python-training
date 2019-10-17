k = int(input())

if k == 3 or k == 5:
    print('YES')
elif k % 3 == 0:
    x = k // 3
    if x * 3 == k:
        print('YES')
    
elif k % 5 == 0:
    x = k // 5
    if x * 5 == k:
        print('YES')
else:
    print('NO')