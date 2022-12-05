X = ['F G V R J L D','S J H V B M P T','C P G D F M H V','Q G N P D M','F N H L J','Z T G D Q V F N','L B D F','N D V S B J M','D L G']

with open("input", 'r') as f:
    Y = [list(map(int, line.strip().split())) for line in f.read().strip().split('\n')]

X1 = list(map(lambda x:x.split(), X))
X2 = list(map(lambda x:x.split(), X))


print('*'*5, 'PART 1', '*'*5)
for N, a, b in Y:
    a = a-1
    b = b-1
    add = X1[a][:N]
    add.reverse()
    X1[b] = add + X1[b]
    X1[a] = X1[a][N:]

part1 = ""
for x in X1:
    part1 += x[0]

print(part1)


print('*'*5, 'PART 2', '*'*5)
for N, a, b in Y:
    a = a-1
    b = b-1
    add = X2[a][:N]
    X2[b] = add + X2[b]
    X2[a] = X2[a][N:]

part2 = ""
for x in X2:
    part2 += x[0]

print(part2)
