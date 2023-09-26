"""
以下の条件を満たす正整数 x を 321-like Number と呼びます。
- x の各桁を上から見ると狭義単調減少になっている。
- すなわち、x が d 桁の整数だとすると、 1≤i<d を満たす全ての整数 i について以下の条件を満たす。
    ・( x の上から i 桁目 ) > ( x の上から i+1 桁目 )
なお、 1 桁の正整数は必ず 321-like Number であることに注意してください。
例えば、 321,96410,1 は 321-like Number ですが、 123,2109,86411 は 321-like Number ではありません。
N が入力として与えられるので、 N が 321-like Number なら Yes 、そうでないなら No と出力してください。
"""
N = int(input())
S = str(N)
len_N = len(S)
list = []
ans = "Yes"

for i in range(len_N):
    list.append(int(S[i]))
    
for i in range(len_N):
    if i+1 < len_N and list[i] <= list[i+1]:
        ans = "No"
        
print(ans)    
