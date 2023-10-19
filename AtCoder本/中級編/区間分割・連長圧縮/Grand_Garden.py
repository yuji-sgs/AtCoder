"""
https://atcoder.jp/contests/abc116/tasks/abc116_c
"""
N = int(input())
h = list(map(int, input().split()))
ans = 0

i = 0
while i < N:
    if h[i] == 0:
        i += 1
        continue
    j = i
    while j < N and h[j] > 0:
        j += 1
    for k in range(i, j):
        h[k] -= 1
    ans += 1

print(ans)
