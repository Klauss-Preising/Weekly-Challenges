"""
Second Weekly Challenge:
This week I want you to create a function that takes one integer n. This function will create a list of the first n prime numbers.
HINT: Prime numbers can only be evenly divided by itself and 1. Prime numbers start at 2.
"""

'''
Uses the primes you already found to figure out if it's a prime number.
All numbers can be described by prime number
Ex:
20 = 2^2 * 5^1
8 = 2^3
12 = 2^2 * 3^1
'''
def isPrime(n, primes = [2]):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in primes:
        if n % i == 0:
            return False
    return True


'''
The loop will continue until the list primes becomes of length of n
count will be added to the list when isPrime comes out true
Give isPrime the primes you have already found
'''
def listPrime(n):
    if n == 0:
        return []
    primes = [2]
    count = 3
    while len(primes) < n:
        if isPrime(count, primes):
            primes.append(count)
        count += 1
    return primes

'''
Other primes
'''
def isPrime_2(n):
    if (n == 1):
        return False
    for i in range(2, (n//2)+1):
        if n % i == 0:
            return False
    return True

def isPrime_3(n):
    def helper(n, count):
        if n//2 < count:
            return True
        if n % count == 0:
            return False
        return helper(n, count+1)
    if (n == 1):
        return False
    return helper(n, 2)


#Tests
print("Tests")
print("\nTesting isPrimes")
print("is 2 a prime", isPrime(2))
print("is 3 a prime", isPrime(3, [2]))
print("is 4 a prime", isPrime(4, [2, 3]))
print("is 4 a prime", isPrime(5, [2, 3]))

print("testing listPrimes")
print("\nList of primes of size 20:", listPrime(20))

print("\nTesting isPrime_2")
print("2:", isPrime_2(2))
print("3:", isPrime_2(3))
print("4:", isPrime_2(4))
print("5:", isPrime_2(5))

print("\nTesting isPrime_3")
print("2:", isPrime_3(2))
print("3:", isPrime_3(3))
print("4:", isPrime_3(4))
print("5:", isPrime_3(5))