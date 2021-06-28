import sys

def fibonacci(n):
    num1 = 0
    num2 = 1
    if n == 0:
        sys.stdout.write('1 0\n')
    else:
        for cnt in range(n - 1):
            tmp = num1 + num2
            num1 = num2
            num2 = tmp
        sys.stdout.write(f'{num1} {num2}\n')

i = int(sys.stdin.readline())
for cnt in range(i):
    n = int(sys.stdin.readline())
    fibonacci(n)
