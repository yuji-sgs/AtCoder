"""
全長 100km のマラソンコースがあります。 
マラソンコースにはスタートから5km おきに給水所が設置されており、スタート地点・ゴール地点とあわせて 21 箇所の給水所があります。
高橋くんは、このマラソンコースの Nkm 地点にいます。 
高橋くんに最も近い給水所は何 km 地点の給水所か求めてください。
この問題の制約のもとで、最も近い給水所が 1 つに定まることが証明できます。
"""
N = int(input())
if N % 5 == 0:
    print(N)
elif N % 5 == 1:
    print(N-1)
elif N % 5 == 2:
    print(N-2)
elif N % 5 == 3:
    print(N+2)
else:
    print(N+1)