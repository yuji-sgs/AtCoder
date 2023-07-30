"""
りんご市場に N 人の売り手と M 人の買い手がいます。
i 番目の売り手は、Ai円以上でならりんごを売ってもよいと考えています。
i 番目の買い手は、Bi円以下でならりんごを買ってもよいと考えています。
次の条件を満たすような最小の整数 X を求めてください。
条件：りんごを X 円で売ってもよいと考える売り手の人数が、りんごを X 円で買ってもよいと考える買い手の人数以上である。
"""
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def check(x):
    idx1 = bisect.bisect_right(A, x)
    idx2 = M - bisect.bisect_left(B, x)
    if idx1 >= idx2:
        return True
    else:
        return False
 
left = 0
right = 10 ** 20
while right - left > 1:
    mid = (left + right) // 2
    ans = check(mid)
    if ans:
        right = mid
    else:
        left = mid
 
print(right)
