"""
A, B, C からなる文字列 S が与えられます。
S は A, B, C を全て含むことが保証されます。
S を左から 1 文字ずつ見ていったときに、はじめて次の条件を満たした状態になるのは、左から何文字目まで見たときですか？
A, B, C が全て 1 回以上出現している
"""
N = int(input())
S = input()
ABC = [False, False, False]

for i in range(N):
    if S[i] == "A":
        ABC[0] = True
    elif S[i] == "B":
        ABC[1] = True
    elif S[i] == "C":
        ABC[2] = True
    if ABC[0] and ABC[1] and ABC[2]:
        print(i+1)
        break
