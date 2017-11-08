import random 

def is_prime(number):
    if number % 2 == 0 and number > 2:
        return False
    else:
        limit = int(number ** (1/2)) + 1
        for i in range(3, limit, 2):
            if number % i == 0:
                return False
        return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    s = 0
    t = 0
    r = b
    old_s = 1
    old_t = 0
    old_r = a
    while r != 0:
        quotient = old_r // r
        old_r, r = r, (old_r - quotient*r)
        old_s, s = s, (old_s - quotient*s)
        old_t, t = t, (old_t - quotient*t)
    if old_r == 1:
        return s+old_s
    else:
        return old_r        

def enciphering_exponent(n, rsa_modulus):
    while True:
        e = random.randint(2, rsa_modulus-1)
        if gcd(e, rsa_modulus) == 1:
            return e

def main():
    while True:
        while True:
            prime1 = int(input("Enter the first prime number: "))
            if is_prime(prime1):
                break
            else:
                print("It isn't a prime number, please retry.")
        while True:      
            prime2 = int(input("Enter the first prime number: "))
            if is_prime(prime1):
                break
            else:
                print("It isn't a prime number, please retry.")
        if prime1 != prime2:
            break
        else:
            print("Prime numbers must not be equal")
    n = prime1*prime2
    rsa_modulus = (prime1-1)*(prime2-1)
    print("n:", n, "rsa_modulus:", rsa_modulus)
    e = enciphering_exponent(n, rsa_modulus)
    d = extended_gcd(e, rsa_modulus)
    print("e:", e, "d:", d)

main()