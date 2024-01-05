"""
正の整数 N が与えられます。 N=2^x*3^yを満たす整数 
x,y が存在するなら Yes 、そうでなければ No と出力してください。
""" 
N = int(input())
Flag = False

for x in range(0, 101):
    for y in range(0, 101):
        if 2**x * 3**y == N:
            Flag = True
            break
        
print("Yes" if Flag else "No")
