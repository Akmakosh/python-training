a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
x = 0
s = 0

for i in range(1000+1):
    x = i
    if (a*x ** 3 + b*x ** 2 + c*x + d) // (x - e) == 0:
        s+=1
print(s)