import sys

N, M = map(int, sys.stdin.readline().split(" "))
board = list()
ans = 64
case1 = [[0 for i in range(8)] for j in range(8)]
case1[0] = case1[2] = case1[4] = case1[6] = "BWBWBWBW"
case1[1] = case1[3] = case1[5] = case1[7] = "WBWBWBWB"

for y_input in range(N):
    board.append(sys.stdin.readline())

def func(x, y, flag):
    global board
    ret = 0
    if flag == 1:
        for j in range(8):
            for i in range(8):
                if board[y + j][x + i] != case1[j][i]:
                    ret += 1
    if flag == 2:
        for j in range(8):
            for i in range(8):
                if board[y + j][x + i] == case1[j][i]:
                    ret += 1
    return ret

for y in range(N - 8 + 1):
    for x in range(M - 8 + 1):
        ans = min(ans, func(x, y, 1), func(x, y, 2))

print(ans)