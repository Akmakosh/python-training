x = int(input())
p = int(input())
y = int(input())
p/=100
year = 1

while (x < y):
    x *= (1+p)
    year += 1
print(year)
