"""
正五角形 P があります。
P の点 S1と点S2を結ぶ線分と、点T1と点T2を結ぶ線分の長さが等しいか判定してください。
""" 
S = input()
T = input()
S1, S2 = S[0], S[1]
T1, T2 = T[0], T[1]
P = "ABCDE"
S_line = abs(P.index(S1) - P.index(S2))
T_line = abs(P.index(T1) - P.index(T2))

if S_line == 1 or S_line == 4:
    S_line = 1
else:
    S_line = 2

if T_line == 1 or T_line == 4:
    T_line = 1
else:
    T_line = 2
    
    
if S_line == T_line:
    print("Yes")
else:
    print("No")
