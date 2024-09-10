# Consider the following three functions, which all compute summations. The first, sum_naturals, computes the sum of natural numbers up to n:
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
        return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k*k*k, k + 1
    return total

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total = total + 8 / ((4 * k - 3) * (4 * k - 1))
        k = k + 1
    return total

def identity(x):
    return 

# They clearly share a common pattern, summation

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    
    return total

