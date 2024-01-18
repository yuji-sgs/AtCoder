"""
1 以上 9 以下の整数 N が入力として与えられます。
数字 N を N 個繋げて得られる文字列を出力してください。
"""
N = int(input())
ans = []

for i in range(N):
    ans.append(N)
    
print(*ans, sep='')
