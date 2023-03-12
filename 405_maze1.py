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

start_position = [[1, 1, 0]];

while len(start_position) > 0:
    x, y, depth = start_position.pop(0);

    if maze[x][y] == 1:
        print(depth);
        break;

    maze[x][y] = 2;

    if maze[x - 1][y] < 2:
        start_position.append([x - 1, y, depth + 1]);
    if maze[x + 1][y] < 2:
        start_position.append([x + 1, y, depth + 1]);
    if maze[x][y - 1] < 2:
        start_position.append([x, y - 1, depth + 1]);
    if maze[x][y + 1] < 2:
        start_position.append([x, y + 1, depth + 1]);
