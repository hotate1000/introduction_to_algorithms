tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]];

def search(position):
    print(position, end=" ");
    # 初めにtree[0][0]が動く（[1,2]の「1」が出力）、
    # 次にtree[1][0]が動く（[3,4]の「3」が出力）、
    # 値が出力できなくなったタイミングでtree[0][1]が動く（[1,2]の「2」が出力）。
    for i in tree[position]:
        search(i);
search(0);