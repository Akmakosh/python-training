a = int(input())
b = int(input())

for i in range (a, b):
    if i == i*i:
        if i * i >= a and i * i <= b:
            print(i*i)