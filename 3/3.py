## conts = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]


##  >>> ord('a')
##  97
##  >>> ord('A')
##  65
##  >>> ord('Z')
##  90
##  >>> ord('z')
##  122

with open('input', 'r') as f:
   conts = list(map(lambda x : x.strip(), f.readlines()))

def get_priority(ch):
    code = ord(ch)
    if(code >= 97 and code <= 122):
        return code - 97 + 1
    return code - 65 + 1 + 26

score = 0;

# Part 1 Code
for cont in conts:
    x, y = set(cont[0:len(cont)//2]), set(cont[len(cont)//2:])
    score += get_priority(list(x.intersection(y))[0])

score2 = 0;

# Part 2 Code
for i in range(len(conts)//3):
    x = set(conts[3*i])
    y = set(conts[3*i+1])
    z = set(conts[3*i+2])
    comm = list(x.intersection(y).intersection(z))[0]
    score2 += get_priority(comm)
print(score2)
