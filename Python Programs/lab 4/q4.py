import math
# lst = list(map(int, input().split()))

# prime factors of the number n


def prime_factors(n):
    while n % 2 == 0:
        print(2, end=" ")
        n = n//2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            print(i, end=" ")
            n = n//i
    if n > 2:
        print(n, end=" ")


n = int(input())
prime_factors(n)
