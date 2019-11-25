n = int(input())
arr = list(map(int, input().split()))
co = 0

for i in range(1, len(arr)-1, 1):
    pr = arr[i-1]
    nex = arr[i+1]
    if pr < arr[i] and nex < arr[i]:
        co +=1
print(co)