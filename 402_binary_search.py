list = [10, 20, 30, 40, 50, 60, 70, 80 ,90];

def binary_search(list, n):
    left = 0;
    right = len(list) - 1;
    while left <= right:
        center = (left + right) // 2;
        if list[center] == n:
            return center;
        elif list[center] < n:
            left = center + 1;
        elif list[center] > n:
            right = center - 1;
    return -1;

print(binary_search(list, 90));