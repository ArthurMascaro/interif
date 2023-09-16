import math


def is_prime(num):
    if 1 < num < 4:
        return True
    elif num < 2 or not num % 2:
        return False
    
    odd_numbers = range(3, int(math.sqrt(num) + 1), 2)
    return not any(not num % i for i in odd_numbers)

nums = int(input())
primes = list()

for i in  range(nums):
    if is_prime(i):
        primes.append(i)

if is_prime(nums):
    if nums not in primes:
        primes.append(nums)

output = ""
for prime in primes:
    output += str(prime) + ' '
print(output.strip())