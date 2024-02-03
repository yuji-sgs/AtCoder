"""
人 1, 人 2,…, 人 N の N 人が一列に並んでいます。
並び方の情報が長さ N の数列 A=(A1,A2,…,AN) として与えられます。
Ai(1≤i≤N) は次のような情報を表しています。
- Ai=−1 のとき、人 i は先頭に並んでいる。
- Ai≠−1 のとき、人 i は人 Aiのすぐ後ろに並んでいる。
列に並んでいる人の番号を先頭から順番に出力してください。
"""
def find_order(N, A):
    # 辞書を初期化
    next_person = {}
    for i in range(1, N + 1):
        if A[i - 1] != -1:
            next_person[A[i - 1]] = i

    # 並び順を再構築
    order = []
    for i in range(1, N + 1):
        if A[i - 1] == -1:
            current = i
            break

    while len(order) < N:
        order.append(current)
        current = next_person.get(current, None)

    # 並び順を出力
    return ' '.join(map(str, order))

N = int(input())
A = list(map(int, input().split()))
print(find_order(N, A))
