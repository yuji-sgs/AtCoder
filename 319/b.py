"""
正整数 N が与えられるので、下記で定まる長さ (N+1) の文字列s0s1…sNを出力してください。
各 i=0,1,2,…,N について、
・1 以上 9 以下の N の約数 j であって、i が N/j の倍数であるものが存在するとき、そのような j のうち最小のものに対応する数字をsiとする。（よって、この場合siは 1 、2 、… 、9 のいずれかである。）
・そのような j が存在しないときsiは - とする。
""" 
N = int(input())
list_j = [j for j in range(1, N+1) if N % j == 0 and 1 <= j <= 9]
ans = []

for i in range(N+1):
    min_j = [] 
    for j in list_j:
        if i % (N // j) == 0:
            min_j.append(j)
    if min_j:
        ans.append(str(min(min_j)))
    else:
        ans.append("-")

print("".join(ans))
