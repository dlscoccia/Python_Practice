#!/usr/bin/env python3
def compute_primes(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for i in answer:
            if i % divisor == 0 and not i == divisor:
                answer.remove(i)

    return answer

print(compute_primes(10))
print(len(compute_primes(200)))
print(len(compute_primes(2000)))



def compute_primes2(bound):
    """
    Return a list of the prime numbers in range(2, bound)
    """
    
    answer = list(range(2, bound))
    for divisor in range(2, bound):
        for stride in range(2 * divisor, bound, divisor):
            if stride in answer:
                answer.remove(stride)
    return answer

print(len(compute_primes2(200)))
print(len(compute_primes2(2000)))
