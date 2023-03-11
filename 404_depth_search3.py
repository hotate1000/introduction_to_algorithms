tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]];

def search(position):
    if len(tree[position])==2:
        search(tree[position][0]);
        print(position, end=' ');
        search(tree[position][1]);
    elif len(tree[position])==1:
        search(tree[position][0]);
        print(position, end=' ');
    else:
        print(position, end=' ')

search(0);