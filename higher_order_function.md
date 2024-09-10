Consider the following three functions, which all compute summations. The first, sum_naturals, computes the sum of natural numbers up to n:
```python
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
```
They share a common pattern of summation. We can make an abstraction for that:
```python
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
```
