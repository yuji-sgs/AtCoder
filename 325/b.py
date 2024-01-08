"""
キーエンスには世界各地に N 個の拠点があり、1 から N までの番号が付けられています。 
拠点 i には Wi人の社員が所属しており、世界標準時で 0 時のとき拠点 i は Xi時です。
あなたはキーエンス全社で 1 時間の会議を開きたいです。 
各社員は、会議の開催時間帯が所属する拠点における 9:00-18:00 の時間帯に完全に含まれる場合にのみ会議に参加できます。
なるべく多くの社員が参加できるように会議の開催時間帯を決めるとき、会議に参加できる社員の数の最大値を求めてください。
""" 
N = int(input())
meetings = []
for i in range(N):
    W, X = map(int, input().split())
    meetings.append((W, X))

ans = 0

for i in range(25):
    cnt = 0
    for w, x in meetings:
        if 9 <= (x + i) % 24 <= 17:
            cnt += w
    ans = max(ans, cnt)    
    
    
print(ans)
