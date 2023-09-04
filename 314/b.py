"""
問題文が長いため、割愛
https://atcoder.jp/contests/abc314/tasks/abc314_b
"""
N = int(input())
data = []
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    data.append((i+1, C, A))
X = int(input())

# Xが含まれるデータを抽出
new_data = []
for i in range(N):
    if X in data[i][2]:
        new_data.append(data[i])
        
if len(new_data) == 0:
    print(0)
    exit()
else:
    # 個数をkeyにしてソート
    new_data.sort(key = lambda x:x[1])

    # 最小個数を取得
    min_C = new_data[0][1]
    ans = []
    for i in range(len(new_data)):
        if new_data[i][1] == min_C:
            ans.append(new_data[i][0])
            
    print(len(ans))
    print(*ans)
