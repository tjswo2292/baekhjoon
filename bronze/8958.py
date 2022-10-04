# # 문제를 맞은 경우 그 문제으 ㅣ점수는 그 문제까지 연속된 0의 개수가 된다.
# # 2차원 배열

# n = []
# count = 0   
# t = int(input()) # test case 길이

# for _ in range(t):
#     n.append(list(map(str, input().split())))

# # 점수
# # 그 전에 o 몇개 있어?

# for i in range(len(n)):
#     for j in range(len(n[i])):
#         # 요소가 o, x 인지 판단
#         if n[i][j] == 'o':
#             if j == 0: # 첫 번째가 o면 무조건 점수는 1이 될 수 밖에 없다
#                 count += 1
#                 break
#             # 연속되는 o이 몇개인지 판단
#             else:
#                 if n[i][-1] == 'o':
                    

# 0가 연속되면 score가 점점 커지는 것을 이용하면 됨

t = int(input())

for _ in range(t):
    ox_list = list(input())
    score = 0
    sum_score = 0
    for ox in ox_list:
        if ox == 'o':
            score += 1
            sum_score += score
        else: score = 0
    print(sum_score)
