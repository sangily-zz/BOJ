T = int(input())
for i in range(T):
    x, y = input().split()
    x = int(x)
    y = int(y)
    tmp = 1
    count = 0
    distance = y - x
    if distance == 1 : count = 1
    elif distance == 2 : count = 2
    else :
        while True:
            distance -= tmp * 2
            count += 2
            if 0 >= distance >= 1 - tmp:
                break
            elif distance < 1 - tmp:
                count -= 1
                break
            tmp += 1          
    print(count)
