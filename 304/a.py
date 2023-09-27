"""
人 1 、人 2 、… 、人 N と番号付けられた N 人が、この順番で時計回りに円卓に座っています。
特に、時計回りで人 N の次の位置には人 1 が座っています。
i=1,2,…,N について、人 i の名前はSi、年齢はAiです。 ここで、異なる 2 人が同じ名前や同じ年齢であることはありません。
年齢が最も小さい人を起点として、座っている位置の時計回りの順番で、N 人全員の名前を出力してください。
"""
N = int(input())
member = []
for i in range(N):
    S, A = input().split()
    A = int(A)
    member.append([S, A])
    
min_age = 10 ** 10
index = 0

for i in range(N):
    min_age = min(min_age, member[i][1])
    index = i if min_age == member[i][1] else index
    
for i in range(N):
    member.append(member[i])

    
for name in range(index, N + index):
    print(member[name][0])
