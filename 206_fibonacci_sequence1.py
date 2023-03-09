def fibonacci_sequence(n):
    if (n==1) or (n==2):
        return 1;
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2);

print(fibonacci_sequence(6));