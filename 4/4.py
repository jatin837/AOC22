X = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
def part1(X):
    cnt = 0
    for (a, b) in X:
        (x1, y1) = tuple(map(int, a.split('-')))
        (x2, y2) = tuple(map(int, b.split('-')))
        if((max(x1, x2) == x1 and min(y1, y2) == y1) or (min(x1, x2) == x1 and max(y1, y2) == y1)):
            cnt+=1

    print('-'*5, 'part 2', '-'*5)
    print(cnt)

def part2(X):
    cnt = 0
    for (a, b) in X:
        (x1, y1) = tuple(map(int, a.split('-')))
        (x2, y2) = tuple(map(int, b.split('-')))
        if not (x1 > y2 or y1 < x2):
            cnt+=1
    print('-'*5, 'part 1', '-'*5)
    print(cnt)

def main():
    with open('input', 'r') as f:
        X = list(map(lambda x:x.split(','), f.read().strip().split('\n')))
    part1(X)
    part2(X)

main()
