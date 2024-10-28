#!/usr/bin/python3

n = 7  # the number I wish to obtain the sqrt for.
tol = 1e-4  # the tolerance in approximation.

sqrt = 1  # initial guess

iter_count = 0
while True:
    iter_count += 1
    sqrt = 0.5 * (sqrt + n / sqrt)
    error = abs(sqrt ** 2 - n)
    if error < tol:
        break

print(f'The approximate square root of {n} is {sqrt:.8f}.')
print(f'Found in {iter_count} iterations.')
