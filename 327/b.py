"""
整数 B が与えられます。
A^A=B であるような正の整数 A が存在するならばその値を、存在しないならば -1 を出力してください。
""" 
B = int(input())
ans = -1

for i in range(1, 1001):
    if i ** i == B:
        ans = i
        break
    
print(ans)
