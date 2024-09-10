# Consider the following three functions, which all compute summations. The first, sum_naturals, computes the sum of natural numbers up to n:
def naturals(x):
    return x

def cubes(x):
    return x * x * x

def pii(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))

def squares(x):
    return x * x

# They clearly share a common pattern, summation

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    
    return total

def sum_cubes(n):
    return summation(n, cubes)

def sum_squares(n):
    return summation(n, squares)

def sum_naturals(n):
    return summation(n, naturals)

print("Enter a number and we'll count its sum in natural, cube, and pi!")
n = int(input("Enter a number: "))

# print("The sum of natural number of 1, 2, 3: ", summation(n, naturals))
print("The sum of cubes of 1, 2, 3: ", sum_cubes(n))
print("The sum of squares of 1, 2, 3: ", sum_squares(n))
print("The sum of natural of 1, 2, 3: ", sum_naturals(n))
