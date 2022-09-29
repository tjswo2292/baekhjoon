# 세 개의 변의 길이가 입력 되면 직각삼각형인지 아닌지 출력
# 마지막 줄에는 0 0 0 출력 되야 함

# 각 변의 길이를 list에 담음
# 직각삼각형인지 아닌지 결과 출력
# list의 길이가 0이면 마지막 줄에 000 출력


# 변의 값을 2차원 배열로 생성
# for i in range(4):
#     mylist.append(list(map(int, input().split())))

while True :
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break

    a *= a
    b *= b
    c *= c
    
    if a+b == c or a+c == b or b+c == a:
        print('right')
    else:
        print('wrong')


# 출력 포멧이 다르게 나오는데 되네
# 프로그래머스랑 많이 다르네