from collections import defaultdict

score = defaultdict(int)

mp = {
    'X' : 'C',
    'Y' : 'A',
    'Z' : 'B',
    'C' : 'Y',
    'A' : 'Z',
    'B' : 'X'
}

defeats = {
    'C' : 'Y',
    'A' : 'Z',
    'B' : 'X'
}

lostto = {
    'C' : 'X',
    'A' : 'Y',
    'B' : 'Z'
}

draw = {
    'C' : 'Z',
    'A' : 'X',
    'B' : 'Y'
}

points={
     'X':1,
     'Y':2,
     'Z':3,
 }

outcome={
    'draw': 3,
    'won': 6,
    'lost': 0,
}

with open('input', 'r') as f:
    matches = list(map(lambda x:x.split(), f.readlines()))

score1 = 0
score2 = 0

for p1, p2 in matches:
    if mp[p2] == p1:
        score1 += points[p2] + outcome['won']
        print(p2, 'defeats', p1)
    elif mp[p1] == p2:
        score1 += points[p2] + outcome['lost']
        print(p1, 'defeats', p2)
    else:
        score1 += points[p2] + outcome['draw']
        print('draw')

for p1, p2 in matches:
    if p2 == 'X':
        score2 += outcome['lost'] + points[defeats[p1]]
    elif p2 == 'Y':
        score2 += outcome['draw'] + points[draw[p1]]
    else:
        score2 += outcome['won'] + points[lostto[p1]]

print(score1, score2)
