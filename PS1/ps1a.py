# 2 is the first prime, but we're skipping that one
num_primes = 1;

# Start checking at 3
odd_checking = 3;

while(num_primes < 1000):
  is_prime = 1;

  # For each test, see if the modulus of the value being checked,
  # with every value less than it, is 0.  If it is, the value isn't
  # prime
  for candidate in range(2, odd_checking):
    if odd_checking % candidate == 0:
      is_prime = 0

  # If it's prime, increment the count and print the value
  if is_prime == 1:
    num_primes += 1
    print(str(odd_checking) + " is prime number " + str(num_primes))

  odd_checking += 2
