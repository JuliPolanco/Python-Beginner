def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")
        
prime_checker(3)
prime_checker(4)

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print("The number is not prime", n, "is divider")
            return False
    print("Es primo")
    return True

is_prime(13)
is_prime(12)
