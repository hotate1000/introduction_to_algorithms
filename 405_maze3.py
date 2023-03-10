maze = [
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    [9, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 9],
    [9, 0, 9, 0, 0, 0, 9, 9, 0, 9, 9, 9],
    [9, 0, 9, 9, 0, 9, 0, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 9, 0, 0, 9, 9, 0, 9, 9],
    [9, 9, 9, 0, 0, 9, 0, 9, 0, 0, 0, 9],
    [9, 0, 0, 0, 9, 0, 9, 0, 0, 9, 1, 9],
    [9, 0, 9, 0, 0, 0, 0, 9, 0, 0, 9, 9],
    [9, 0, 0, 9, 0, 9, 0, 0, 9, 0, 0, 9],
    [9, 0, 9, 0, 9, 0, 9, 0, 0, 9, 0, 9],
    [9, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 9],
    [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
]

move = [[1,0],[0,1],[-1,0],[0,-1]];

# depthは移動回数、移動方向。
x,y,depth,d = 1,1,0,0;

while maze[x][y] != 1:
    maze[x][y] = 2;
    for i in range(len(move)):
        j = (d + i - 1) % len(move);
        if maze[x + move[j][0]][y + move[j][1]] < 2:
            x += move[j][0];
            y += move[j][1];
            d = j;
            depth += 1;
            break;
        elif maze[x + move[j][0]][y + move[j][1]] == 2:
            x += move[j][0];
            y += move[j][1];
            d = j;
            depth -= 1;
            break;
print(depth);
