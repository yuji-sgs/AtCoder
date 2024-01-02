"""
N 人のプレイヤーが参加するプログラミングコンテスト World Tour Finals が行われており、競技時間の半分が過ぎました。 
このコンテストでは M 問の問題が出題されており、問題 i の点数 Aiは 500 以上 2500 以下の 100 の倍数です。
各 i=1,…,N について、プレイヤー i がどの問題を既に解いたかを表す文字列 Siが与えられます。
Siは o, x からなる長さ M の文字列で、Siの j 文字目が o のときプレイヤー i は問題 j を既に解いており、x のときまだ解いていません。 ただし、どのプレイヤーもまだ全ての問題を解いてはいません。
プレイヤー i の総合得点は、解いた問題の点数の合計に、ボーナス点 i 点を加えた点数として計算されます。
さて、各 i=1,…,N について以下の質問に答えてください。
- プレイヤー i がまだ解いていない問題を少なくとも何問解くことで、プレイヤー i の総合得点が他のプレイヤー全員の現在の総合得点を上回ることができますか？
なお、問題文中の条件と制約から、プレイヤー i が全ての問題を解くことで、他のプレイヤー全員の現在の総合得点を上回ることができることが証明できます。 このことから、答えは常に定義されることに注意してください。
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
solve_question = [input() for _ in range(N)]
current_score =[0] * N

for i in range(N):
    current_score[i] += i+1
    for j in range(M):
        if solve_question[i][j] == "o":
            current_score[i] += A[j]
            
for i in range(N):
    ans = 0
    not_solve = sorted([A[j] for j in range(M) if solve_question[i][j] == "x"], reverse=True)
    score = current_score[i]
    for k in range(len(not_solve)):
        if score < max(current_score):
            score += not_solve[k]
            ans += 1
    print(ans)
