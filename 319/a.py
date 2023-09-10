"""
AtCoder では、レーティング上位 10 人のハンドルネームには金色の冠が、上位 1 人のハンドルネームには白金色の冠が表示されます。
このコンテストが開始した時点で、アルゴリズム部門での上位 10 人に入っているプレイヤーのハンドルネームとレーティングは以下のようになっています。
tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
上記のプレイヤーのハンドルネーム S が与えられるので、その人のレーティングを出力してください。
"""
S = input()
rating_dict = {
    "tourist": 3858, 
    "ksun48": 3679,
    "Benq": 3658,
    "Um_nik": 3648,
    "apiad": 3638,
    "Stonefeang": 3630,
    "ecnerwala": 3613,
    "mnbvmar": 3555,
    "newbiedmy": 3516,
    "semiexp": 3481
}

print(rating_dict[S])
