"""
正整数 D が与えられます。
非負整数 x,y に対する ∣x^2+y^2−D∣ の最小値を求めてください。
"""
import math
D = int(input())

ans = 1 << 60
for x in range(0, 2 * 10**6+1):
    yy = math.isqrt(abs(D - x * x))
    for y in range(yy - 10, yy + 11):
        ans = min(ans, abs(x * x + y * y - D))
        
print(ans)
