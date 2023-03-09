
import math

def calculate_prime_numbers(n):
    if n <= 1:
        return False; 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False;
    return True;

for i in range(200):
    if calculate_prime_numbers(i):
        print(i, end= ' ');
