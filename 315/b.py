"""
AtCoder 国の暦では、一年は 1,2,…,M 番目の月の M か月からなり、そのうち i 番目の月は1,2,…,Di番目の日のDi日からなります。
さらに、 AtCoder 国の一年の日数は奇数、即ちD1+D2+⋯+DMは奇数です。
一年の真ん中の日は何番目の月の何番目の日か求めてください。
言い換えると、1 番目の月の1 番目の日を1 日目としたときの(D1+D2+⋯+DM+1)/2 日目が何番目の月の何番目の日かを求めてください。
"""
M = int(input())
D = list(map(int, input().split()))
mid = (sum(D) + 1) // 2

month = 0
day = (sum(D) + 1) // 2

while mid > 0:
    mid -= D[month]
    month += 1
    
for i in range(month-1):
    day -= D[i]
    
print(month, day)
