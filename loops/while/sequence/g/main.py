n = int(input())
mx1 = n
n = int(input())
mx2 = n
if mx1 < mx2:
    mx1, mx2 = mx2, mx1

while n != 0:
    if mx1 < n:
        mx2 = mx1
        mx1 = n
    elif mx2 < n and mx1 != n:
        mx2 = n  
    n = int(input())
print(mx2)