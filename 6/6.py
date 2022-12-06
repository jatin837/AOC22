with open('input', 'r') as f:
    X = f.read().strip()

print("*"*5, 'PART 1', "*"*5)

i = 3
while i < len(X):
    if(len(set(X[i-3:i+1])) == 4):
        print(i+1)
        break
    i+=1

print("*"*5, 'PART 2', "*"*5)
i = 13
while i < len(X):
    if(len(set(X[i-13:i+1])) == 14):
        print(i+1)
        break
    i+=1


