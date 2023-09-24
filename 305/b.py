"""
問題文省略
https://atcoder.jp/contests/abc305/tasks/abc305_b
"""
p, q = input().split()
dist = [3, 1, 4, 1, 5, 9]
dict_ABC = {"A": 0, "B": 1, "C": 2, "D":3, "E":4, "F":5, "G":6}
ans = sum(dist[dict_ABC[p]:dict_ABC[q]])
if ans != 0:
    print(ans)
else:
    ans = sum(dist[dict_ABC[q]:dict_ABC[p]])
    print(ans)
