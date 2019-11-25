n = int(input())
m = int(input())

while n != m:
    if n % 2 == 0 and n//2>=m:
        n //= 2
        print(':2')
    else:
        n-=1
        print('-1')

    