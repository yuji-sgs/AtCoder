"""
AtCoder 国では、1 年が N か月からなる暦を使っています。 
i 月 (1≤i≤N) は、i 月 1 日から i 月 Di日までの Di日からなります。
AtCoder 国において、1 年のうち日付がゾロ目になる日が何日あるか求めてください。
ただし、i 月 j 日 (1≤i≤N,1≤j≤Di) の日付がゾロ目になるとは、1 種類の数字だけを用いて i と j を十進法で表すことができることをいいます。
""" 
def is_zorome(i, j):
    day = str(i) + str(j)
    tmp = set()
    for d in day:
        tmp.add(d)
    if len(tmp) == 1:
        return True

N = int(input())
D = list(map(int, input().split()))
ans = 0

for i in range(N):
    for j in range(D[i]):
        day = i+1
        month = j+1
        if is_zorome(day, month):
            ans += 1
        
print(ans)
