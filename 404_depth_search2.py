tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]];

def search(position):
    for i in tree[position]:
        search(i);
    print(position, end=' ');

search(0);