# n x m, cctv 5
# 6 : 벽, 0 : 빈칸
# 회전하는 건 CCTV1, 2, 3, 4

# 1. cctv 위치 구하기
# 2. iter cctv, iter 회전 방향 0, 90, 180, 270
# 3. 그 때의 최소 값 구하기


if __name__ == '__main__':
    cctv1 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    cctv2 = [[(1, 0), (-1, 0)], [(0, -1), (0, 1)]]
    cctv3 = [[(1, 0), ]]