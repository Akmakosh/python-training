x = int(input())
s = 0
men = x

while x!= 0:
    x = int(input())
    if men < x:
        s+=1
    men = x
print(s)
