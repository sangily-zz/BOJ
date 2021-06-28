a = input().split(" ", 2)
for i in range(3):
    a[i] = int(a[i])
print((a[0] + a[1]) % a[2])
print((a[0] % a[2] + a[1] % a[2]) % a[2])
print((a[0] * a[1]) % a[2])
print(((a[0] % a[2]) * (a[1] % a[2])) % a[2])
