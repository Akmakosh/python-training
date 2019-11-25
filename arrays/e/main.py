n = int(input())
arr = list(map(int, input().split()))
co = ''

for i in range(1, len(arr), 1):
    pr = arr[i-1]
    if (pr < 0 and arr[i]<0) or (pr > 0 and arr[i] > 0):
        co = 'YES'
    else:
        co = 'NO'
print(co)