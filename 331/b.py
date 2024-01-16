"""
スーパーマーケットで卵のパックが売られています。
卵 6 個入りのパックは S 円、卵 8 個入りのパックは M 円、卵 12 個入りのパックは L 円です。
どのパックも何パックでも購入できるとき、N 個以上の卵を買うために必要な最小の金額を求めてください。
""" 
N, S, M, L = map(int, input().split())
ans = 1 << 60

for i in range(18):
    for j in range(14):
        for k in range(10):
            if N <= 6* i + 8 * j + 12 * k:
                ans = min(ans, S * i + M * j + L * k)
                
print(ans)
