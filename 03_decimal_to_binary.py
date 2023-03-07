def decimal_to_binary(n,m):
    answer='';
    while n > 0:
        answer = str(n % m) + answer;
        n = n // m;
    return answer;

print(decimal_to_binary(19,2));
print(decimal_to_binary(18,2));
