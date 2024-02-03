"""
チーム高橋とチーム青木が N 回の試合を行いました。 
i 回め (1≤i≤N) の試合ではチーム高橋が Xi点、チーム青木が Yi点を獲得しました。
N 回の試合で獲得した得点の合計がより多いチームの勝ちです。
どちらのチームが勝ったか出力してください。 ただし、獲得した得点の合計が等しい場合は引き分けとなります。
"""
N = int(input())
X, Y = 0, 0

for _ in range(N):
    x, y = map(int, input().split())
    X += x
    Y += y
    
if X > Y:
    print("Takahashi")
elif X < Y:
    print("Aoki")
else:
    print("Draw")
