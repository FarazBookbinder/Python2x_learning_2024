def fib(n):
num1 = int(0)
num2 = int(1)
for i in range(2,n):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
