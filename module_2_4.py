numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primers = []
for i in numbers:
    if i != 1:
        is_prime = True
        for j in range( 2, i ):
            if i % j == 0:
                is_prime = False
                break
        if not is_prime:
            not_primers.append(i)
        else:
          primes.append(i)
print('Primes = ', primes)
print('Not_primers = ', not_primers)
