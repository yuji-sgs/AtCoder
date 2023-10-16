"""
カツサンドくんはオムライスが好きです。
他にも明太子や寿司、クリームブリュレやテンダーロインステーキなどが好きで、これらの食べ物は全て、誰もが好きだと信じています。
その仮説を証明するために、N 人の人に M 種類の食べ物について好きか嫌いかの調査を行いました。
調査の結果、i 番目の人はAi1番目,Ai2番目,...,AiKi番目の食べ物だけ好きだと答えました。
N 人全ての人が好きだと答えた食べ物の種類数を求めてください。
"""
N, M  = map(int, input().split())
kinds = [0] * 31
for i in range(N):
    num_list = list(map(int, input().split()))
    A = num_list[1:]
    for a in A:
        kinds[a] += 1
        
print(kinds.count(N))
