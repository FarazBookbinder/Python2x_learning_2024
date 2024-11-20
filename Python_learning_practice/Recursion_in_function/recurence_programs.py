# Write a recurrsive function to calculate the sum of first n naturals numbers


def calculate_sum(n):
    if n == 0:
        return 0
    sum = calculate_sum(n-1) + n # first call calculate n-1(4-1) = 3 means it calculate (1+2+3) + n(4)
    print(sum)
    return sum

calculate_sum(4)