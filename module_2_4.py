numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(2, 16):
     is_prime = 0
     for j in range(1, 16):
          if i % j == 0 and i != j and j != 1:
               is_prime += 1
     if is_prime == 0:
          primes.append(i)
     else:
          not_primes.append(i)
print(primes)
print(not_primes)