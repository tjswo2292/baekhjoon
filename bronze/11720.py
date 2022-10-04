# n 개의 숫자가 공백 없이 쓰여있다

n = int(input())
num = input()
sum = 0

for i in range(n):
    sum += int(num[i])

print(sum)