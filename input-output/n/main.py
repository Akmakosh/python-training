n = int(input())

s = 540
l = 45
ob = 5
eb = 15
m = n % 2

y = s + (l * n) + ob * ((n+1) // 2) + eb * (n // 2) - 5 - (1 - m) *10

print((y %1440 // 60), (y % 60))