import math

def calculate_prime_numbers(n):
    if n <= 1:
        return [];
    prime = [2];
    limit = int(math.sqrt(n));

# 「data = [i + 1 for i in range(20)]」、iは0、1～20のリストを作成する
    data = [i + 1 for i in range(2, n, 2)];
    # 25なら5まで
    while limit > data[0]:
        prime.append(data[0]);
        # 現在のdata[0]の値は割れるため確実に消え、data[0]の値が変わる
        data = [j for j in data if j % data[0] != 0]
    return prime + data

print(calculate_prime_numbers(20));
