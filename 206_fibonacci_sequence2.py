data = {1:1, 2:1};

def fibonacci_sequence(n):
    if n in data:
        return data[n];
    data[n] = fibonacci_sequence(n-2) + fibonacci_sequence(n-1)
    return data[n]

print(fibonacci_sequence(6));
