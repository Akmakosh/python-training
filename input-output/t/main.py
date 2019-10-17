h = int(input())

f = h // 100
s = h % 100
r = s % 10 * 10 + s // 10
print((f - r) + 1)
