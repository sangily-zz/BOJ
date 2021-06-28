i = int(input())
for n in range(i):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    sum = (r1 + r2) ** 2
    diff = (r1 - r2) ** 2
    if distance == 0 and diff == 0:
        print(-1)
    elif distance != 0 and diff < distance < sum:
        print(2)
    elif distance != 0 and (sum == distance or diff == distance):
        print(1)
    else:
        print(0)
