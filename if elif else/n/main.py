a = int(input())
b = int(input())

if a == 0 and b == 0:
    print('INF')
elif a == 0 and b!=0:
    print('NO')
elif a != 0 and b == 0:
    print(0)
elif a != 0 and b != 0:
    print(-b / a)

