# Any function which is call it self called recursion.

# WAF to print reverse value from the n(Whatever Given value) value.

# def main_call(n):
#     if n == 0:
#         return
#     print(n)
#     main_call(n-1)
#
# main_call(7)

# WAP define a recursion function which calculate a factorial of n value.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = factorial(n-1) * n
        print(f"factorial({n}) = {result}")
        return result

factorial(5)

