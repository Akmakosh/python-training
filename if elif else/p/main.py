a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c > a and d > b:
    e = c - a 
    f = d - b
    print(e, f)
elif c == a and d > b:
    e = c - a 
    f = d - b
    print(e, f)
elif c > a and d == b:
    e = c - a 
    f = d - b
    print(e, f)
elif c > a and d < b:
    e = c - a 
    if e == 1:
        ex = e - 1
        f = d - b + e * 100
        print(ex, f)
    elif e > 1:
        ex = e - 1
        f = d - b + 1 * 100
        print(ex, f)
elif c < a and d > b:
    e = c - a
    f = d - b
    print(e,f)
elif c < a and d < b:
    e = c - a
    f = b - d
    print(e,f)
