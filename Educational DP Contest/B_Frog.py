"""
N 個の足場があります。 足場には 1,2,…,N と番号が振られています。 各 i （1≤i≤N) について、足場i の高さはhiです。
最初、足場 1 にカエルがいます。 カエルは次の行動を何回か繰り返し、足場 N まで辿り着こうとしています。
・足場 i にいるとき、足場 i+1, i+2 …, i+K のどれかへジャンプする。 このとき、ジャンプ先の足場を j とすると、コスト |hi-hj|を支払う。
カエルが足場 N に辿り着くまでに支払うコストの総和の最小値を求めてください。
"""
N, K= map(int, input().split())
h = list(map(int, input().split()))

INF = 10 ** 9
dp = [INF] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    for j in range(1, K+1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))
    
print(dp[N-1])
