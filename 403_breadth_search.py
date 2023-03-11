tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]];

data = [0];
while len(data) > 0:
    # 一番初めに0の値が入り、次にtree[0]、tree[1]の値を確認する。
    position = data.pop(0);
    print(position, end=' ');
    # tree[0]だとdataに1、2の値は代入される。
    for i in tree[position]:
        data.append(i);