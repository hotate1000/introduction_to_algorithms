M, N = 6, 5;

# 二重配列を作成している。
route = [[0 for i in range(N + 1)] for j in range(M + 1)];

print(route);

for i in range(M + 1):
    route[i][0] = 1;

print(route);

for i in range(1, N + 1):
    route[0][i] = 1;

print(route);

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # print(route[j-1][i]);
        # print(route[j][i-1]);
        route[j][i] = route[j-1][i] + route[j][i-1];

print(route[M][N]);
