import sys

sys.setrecursionlimit(10**9)

# 첫줄 테이스케이스 개수 및 정보 입력
T = int(sys.stdin.readline())

for t in range(T):    
    M, N, K = map(int, sys.stdin.readline().split(" "))

    # table 초기화
    table = [[0 for x in range(M)] for y in range(N)]

    # table 구성
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split(" "))
        table[y][x] = 1

    # 상하좌우 탐색 함수 정의
    def search(x, y):
        global table
        table[y][x] = 0
        if (x - 1 >= 0 and table[y][x - 1] == 1):
            search(x - 1, y)
        if (y - 1 >= 0 and table[y - 1][x] == 1):
            search(x, y - 1)
        if (x + 1 < M and table[y][x + 1] == 1):
            search(x + 1, y)
        if (y + 1 < N and table[y + 1][x] == 1):
            search(x, y + 1)
        
    # table 조회 및 탐색 실행
    worm = 0
    for x in range(M):
        for y in range(N):
            if table[y][x] == 0: continue
            else:
                worm += 1
                search(x, y)

    sys.stdout.write(f'{worm}\n')