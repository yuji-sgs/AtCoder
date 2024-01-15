"""
長さ N の整数列 A=(A1,A2,…,AN) 及び整数 L,R が与えられます。ここで L,R は L≤R を満たします。
i=1,2,…,N について以下の 2 つの条件を共に満たす整数 Xiを求めてください。なお、求める整数は常に一意に定まります。
- L≤Xi≤R
- L 以上 R 以下であるようなどの整数 Y についても ∣Xi−Ai∣≤∣Y−Ai∣ を満たす
""" 
N, L , R = map(int, input().split())
A = list(map(int, input().split()))
ans = []

for i in range(N):
    if A[i] <= L:
        ans.append(L)
    elif A[i] >= R:
        ans.append(R)
    else:
        ans.append(A[i])
        
print(*ans)
