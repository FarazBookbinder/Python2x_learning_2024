"""
for num in range(1,30):
    if num % 2 == 0:
        print(f"this is the even number {num}")
    else:
        print(f"This is the odd number {num}")
"""
## To use above example use another way with "continue"
for num in range(1,30):
    if num % 2 == 0:
        print(f"this is the even number {num}")
        continue
    print(f"This is the odd number {num}")