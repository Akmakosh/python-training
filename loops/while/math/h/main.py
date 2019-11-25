n =int(input())
i = 1
a = 0
b = 1
while i<n:
    a, b = b, a+b
    i+=1
print(b)