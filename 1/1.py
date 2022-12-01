with open('input', 'r') as f:
    cont = f.read()
    nums = cont.split('\n\n')

    nums = [list(map(int, x.strip().split('\n'))) for x in nums]
    part1 = [sum(num) for num in nums]
    part1.sort()
    part2 = part1[-1] + part1[-2] + part1[-3]
    print(part2)
