# 정수 10개를 입력 받은 뒤, 이를 42로 나눈 나머지를 구하기
# 그 다음 서로 다른 값이 몇개 있는지 출력 -> 중복되는 값중 하나를 뺀다

n_list = []
remainder = [] # 나머지
divide = 42

for _ in range(10):
    n_list.append(int(input()))

for i in range(len(n_list)):
    remainder.append(n_list[i] % divide)

remainder = list(set(remainder))

print(len(remainder))