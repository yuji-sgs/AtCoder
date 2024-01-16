"""
AtCoder 国の暦では、1 年は 1 月から M 月までの M ヶ月からなり、どの月も 1 日から D 日までの D 日からなります。
AtCoder 国の暦で y 年 m 月 d 日の翌日は何年何月何日であるか求めてください。
"""
M, D = map(int, input().split())
y, m, d = map(int, input().split())

if d == D:
    d = 1
    if m == M:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1
    
print(y, m, d)
