import sys

#Implementation of the Sieve of Eratosthenes

#Returns a list of all prime numbers less than "upper_limit"

#Works by generating a list of booleans for each positive integer less than upper limit and then crossing off multiples of primes

#E.g. first it eliminates all even numbers (except 2) then all multiples of 3 (that weren't already eliminated) then 5, etc.

#Used in many project euler problems, so I usually just import and reuse this

def Sieve_Primes(upper_limit):
    is_prime = [True] * upper_limit
    is_prime[0] = is_prime[1] = False
    
    for i in range(4, upper_limit, 2):
        is_prime[i] = False
    
    for i in range(3, upper_limit, 2):
        if is_prime[i]:
            for j in range(i*i, upper_limit, 2*i):
                is_prime[j] = False
    
    return [p for p in range(2, upper_limit) if is_prime[p]]
	
	
	
if __name__ == "__main__":
	n = int(sys.argv[1])
	primes = Sieve_Primes(n)
	print(primes)