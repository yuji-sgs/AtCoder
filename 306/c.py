"""
1,2,…,N がちょうど 3 回ずつ現れる長さ 3N の数列 A=(A1,A2,…,A3N) が与えられます。
i=1,2,…,N について、A の中にある i のうち真ん中にあるものの添字を f(i) と定めます。 
1,2,…,N を f(i) の昇順に並べ替えてください。
"""
N = int(input())
A = list(map(int, input().split()))
A_index = [0] * N
ans = []

for i in range(3*N):
    A_index[A[i]-1] += 1
    if A_index[A[i]-1] == 2:
        ans.append(A[i])
        
print(*ans)
