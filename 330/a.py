"""
N 人の人 1,2,…,N がある試験を受け、人 i は Ai点を取りました。
この試験では、 L 点以上を取った人のみが合格となります。
N 人のうち何人が合格したか求めてください。
"""
N, L = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
    if A[i] >= L:
        ans += 1
        
print(ans)
