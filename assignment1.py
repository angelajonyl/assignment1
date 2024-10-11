#Assignment 1
#Angela Jonyl Reyes

def is_prime(n):
    if n <= 1:  #any number less than or equal to 1 cannot be prime
        return False
    for i in range(2, int(n**0.5) + 1):  # gives the square root of n, and int(n**0.5) + 1 ensures we check up to the square root.
        if n % i == 0:  # Checks whether n is divisible by i. If n % i == 0, it means that i divides n without any remainder, and therefore n cannot be a prime number
            return False
    return True


def find_next_prime(n):
    i = n + 1
    while True:
        if is_prime(i):
            return i
        i += 1 # If i is not prime, the function increments i by 1 (i += 1) and checks the next number


def find_previous_prime(n):  # Find the largest prime number that is less than a given number n
    if n <= 2:   # Checks if n is less than or equal to 2. Since the smallest prime number is 2
        return None
    for i in range(n-1, 1, -1):  # Iterates through the numbers starting from n-1 down to 2
        if is_prime(i):
            return i
    return None


def prime_factors(n):
    factors = []
    for i in range(1, n+1): # iterates over all integers i from 1 up to and including n
        if n % i == 0:  # For each value of i, the condition n % i == 0 checks if n is divisible by i
            factors.append(i)
    return factors


def prime_info(num):
    # Previous prime
    previous_prime = find_previous_prime(num)
    
    # Check if the number is prime
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        factors = prime_factors(num)
        print(f"{num} is not a prime number. Its factors are: {factors}")
    
    
    # Next prime
    next_prime = find_next_prime(num)
    
    if previous_prime:
        print(f"The prime number before {num} is {previous_prime}.")
    else:
        print(f"There is no prime number before {num}.")
    
    print(f"The next prime number after {num} is {next_prime}.")


def get_valid_number():
    while True:
        try:
            user_input = input("Please enter the number to check: ")
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    num = get_valid_number()
    prime_info(num)

if __name__ == "__main__":
    main()


# references: 
# https://www.programiz.com/python-programming/examples/prime-number
# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/
# https://www.programiz.com/python-programming/examples/factor-number