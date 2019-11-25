s = 0
r = 0
l = 0
n = int(input())

for i in range (n):
    x = int(input())
    if x == 0:
        s+=1
    elif x > 0:
        r+=1
    elif x < 0:
        l+=1

print(s, r, l)