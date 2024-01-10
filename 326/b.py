"""
3 桁の正整数であって、百の位の数と十の位の数の積が一の位の数と等しいものを 326-like number と呼びます。
例えば 326,400,144 は 326-like number であり、623,777,429 は 326-like number ではありません。
整数 N が与えられるので、N 以上の最小の 326-like number を求めてください。なお、制約の条件下で答えは必ず存在します。
""" 
N = int(input())
ans = N

for i in range(920):
    N_list = str(ans)
    if int(N_list[0]) * int(N_list[1]) == int(N_list[2]):
        break
    else:
        ans += 1
        
print(ans)
