a = int(input())
i = 1
y = 0
z = 1
while z<a:
    y, z = z, y+z
    i+=1

if a != z:
    print(-1)
else:
    print(i)