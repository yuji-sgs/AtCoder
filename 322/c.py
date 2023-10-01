"""
AtCoder 王国では、これから N 日間のお祭りが開催されます。
そのうち、A1日目、A2日目、…、AM日目の M 日では花火が上がります。ここで、お祭りの最終日には花火が上がることが保証されます。(つまり、AM=N が保証されます。)
i=1,2,…,N に対して、以下の問題を解いてください。
i 日目以降で初めて花火が上がるのは、i 日目から数えて何日後か？ただし、i 日目に花火が上がる場合 0 日後とする。
"""
N, M = map(int, input().split())
A = set(map(lambda x:int(x) - 1, input().split()))

day = [0] * N
for i in range(N - 1, -1, -1):
    if i not in A:
        day[i] += day[i + 1] + 1

for d_i in day:
    print(d_i)
