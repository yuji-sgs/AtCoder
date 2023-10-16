"""
低橋くんはプログラミングコンテストサイト「LowCoder」を作り、サービスを開始しました。
今日の時点では、LowCoder にはユーザはいません。
今日から数えて i(1≤i≤N) 日後には、ユーザ名Siを希望するユーザが登録申請を行います。
申請を行った時点でユーザ名が Siであるユーザが存在する場合、その登録申請は無視されます。
そのようなユーザが存在しない場合は登録申請が受理され、LowCoder にそのユーザが登録されます。
何日目の登録申請が受理されるかを求めてください。
"""
from collections import defaultdict

N = int(input())
user_list = defaultdict(int)

for i in range(N):
    S = input()
    if not user_list[S]:
        user_list[S] = 1
        print(i + 1)
