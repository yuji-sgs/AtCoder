"""
あなたは、joisinoお姉ちゃんと以下のようなゲームをしています。
- 最初、何も書いていない紙がある。
- joisinoお姉ちゃんが一つの数字を言うので、その数字が紙に書いてあれば紙からその数字を消し、書いていなければその数字を紙に書く。これを N 回繰り返す。
- その後、紙に書かれている数字がいくつあるかを答える。
joisinoお姉ちゃんが言った数字が、言った順番に A1,...,ANとして与えられるので、ゲーム終了後に紙に書かれている数字がいくつあるか答えてください。
"""
from collections import defaultdict

N = int(input())
num_dict = defaultdict(int)
for i in range(N):
    num = int(input())
    num_dict[num] += 1

ans = 0
for key, value in num_dict.items(): # 辞書内のキーと値のペアをタプルとして繰り返し処理
    if value % 2 == 1:
        ans += 1
        
print(ans)
