x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))

# 원점으로 가는 거리 구해야 함
    # 원점으로 가는 거리는 x, y 자체가 됨
# 주어진 좌표로 가는 거리
    # w-x , h-y