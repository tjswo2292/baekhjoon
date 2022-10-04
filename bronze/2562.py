# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는

# 입력 : 서로 다른 자연수 9개
# 출력 : 최댓값, 몇 번째 수인지


n = []
# n = list(map(int, input().split())) 이건 왜 안되는지
for i in range(9):
    n.append(int(input()))

print(max(n))
print(n.index(max(n)) + 1)