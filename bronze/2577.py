n = []
mult = 1

for _ in range(3):
    n.append(int(input()))

for i in range(len(n)):
    mult *= n[i]

result = list(str(mult))

for i in range(10):
    print(result.count(str(i)))