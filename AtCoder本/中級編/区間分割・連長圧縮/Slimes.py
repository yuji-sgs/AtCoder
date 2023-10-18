"""
https://atcoder.jp/contests/abc143/tasks/abc143_c
"""
N = int(input())
S = input()
slimes = []
i = 0
while i < N:
    j = i + 1
    while j < N and S[i] == S[j]:
        j += 1
    slimes.append(S[i:j])
    i = j
    
print(len(slimes))
