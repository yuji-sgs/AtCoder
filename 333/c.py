"""
十進法ですべての桁の数字が 1 である整数をレピュニットと呼びます。レピュニットを小さい順に並べると 1,11,111,… です。
ちょうど 3 つのレピュニットの和として表せる整数のうち N 番目に小さいものを求めてください。
"""
def generate_repunit(length):
    return int('1' * length)

N = int(input())
repunit = set()
for i in range(1, 20):
    for j in range(1, 20):
        for k in range(1, 20):
            repunit.add(generate_repunit(i) + generate_repunit(j) + generate_repunit(k))
            
repunit = sorted(list(repunit))
print(repunit[N - 1])
