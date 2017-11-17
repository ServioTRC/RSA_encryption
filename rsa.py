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
    while r > 0:
        quotient = old_r // r
        old_r, r = r, (old_r - quotient*r)
        old_s, s = s, (old_s - quotient*s)
        old_t, t = t, (old_t - quotient*t)
    res = s+old_s       
    return res

def enciphering_exponent(n, rsa_modulus):
    while True:
        '''e = 47
        return e'''
        e = random.randint(2, rsa_modulus-1)
        if gcd(e, rsa_modulus) == 1:
            return e

def encrypter(message, e, n):
    message_encrypt = []
    for letter in message:
        message_encrypt.append(ord(letter) ** e % n)
    return message_encrypt

def decrypter(message, d, n):
    message_decrypt = ""
    for val in message:
        message_decrypt += chr(int(val ** d % n))
    return message_decrypt

def main():
    while True:
        while True:
            prime1 = int(input("Enter the first prime number: "))
            if is_prime(prime1):
                break
            else:
                print("It isn't a prime number, please retry.")
        while True:      
            prime2 = int(input("Enter the second prime number: "))
            if is_prime(prime2):
                break
            else:
                print("It isn't a prime number, please retry.")
        if prime1 != prime2:
            break
        else:
            print("Prime numbers must not be equal")
    
    n = prime1*prime2
    rsa_modulus = (prime1-1)*(prime2-1)
    while True:
        e = enciphering_exponent(n, rsa_modulus)
        d = extended_gcd(e, rsa_modulus)
        if d > 0:
            break
    print("RSA modulus:", rsa_modulus)
    print("Public key values:\n\tn =", n, "\te =", e)
    print("Private key values:\n\tn =", n, "\td =", d)
    message = input("Insert the message in 'message' to encrypt : ")
    message_encrypt = encrypter(message, e, n)
    print("Encrypted message: ", end="")
    #print(message_encrypt)
    for val in message_encrypt:
        print(chr(val%128), end="")
    '''for val in message_encrypt:
        print(val, end="")'''
    print()
    message = decrypter(message_encrypt, d, n)
    print("Decrypted message:", message)

if __name__ == '__main__':
    main()
