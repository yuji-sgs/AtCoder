"""
2 つの整数 K,S が与えられます。
3 つの変数 X,Y,Z があり、0≦X,Y,Z≦K を満たす整数の値を取ります。
X+Y+Z=S を満たす X,Y,Z への値の割り当ては何通りありますか。
"""
K, S = map(int, input().split())
count = 0
for x in range(K+1):
    for y in range(K+1):
        z = S - x - y
        if 0 <= z <= K:
            count += 1
            
print(count)
