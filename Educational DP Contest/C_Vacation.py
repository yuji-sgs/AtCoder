"""
明日から太郎君の夏休みが始まります。 太郎君は夏休みの計画を立てることにしました。
夏休みは N 日からなります。 各 i (1≤i≤N) について、i 日目には太郎君は次の活動のうちひとつを選んで行います。
・A: 海で泳ぐ。 幸福度aiを得る。
・B: 山で虫取りをする。 幸福度biを得る。
・C: 家で宿題をする。 幸福度ciを得る。
太郎君は飽き性なので、2 日以上連続で同じ活動を行うことはできません。
太郎君が得る幸福度の総和の最大値を求めてください。
"""
N = int(input())
active = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]
dp[0] = active[0]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = max(dp[i-1][1], dp[i-1][2]) + active[i][j]
        elif j == 1:
            dp[i][j] = max(dp[i-1][0], dp[i-1][2]) + active[i][j]
        else:
            dp[i][j] = max(dp[i-1][0], dp[i-1][1]) + active[i][j]
        
            
print(max(dp[N-1]))
