#!/bin/python3

import sys

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]


def prime_factors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
    if n > 1:
        if n not in factors:
            factors[n] = 0
        factors[n] += 1
    return factors

    

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    usedPrime = list(filter(lambda x: x <= n, primes))
    dictUsedPrime = {}
    value = 1
    
    #filling the dictUsedPrime dictionary
    for p in usedPrime:
        dictUsedPrime[p] = 1
        value *= p
    
    for i in range(n,1,-1):
        
        if value % i == 0:
            continue
        
        iFactors = prime_factors(i)
        for p, occ in iFactors.items():
            if p not in dictUsedPrime:
                value *= pow(p,occ)
                dictUsedPrime[p] = occ
            else:
                if occ > dictUsedPrime[p]:
                    value *= pow(p,occ-dictUsedPrime[p])
                    dictUsedPrime[p] = occ
    print(value)