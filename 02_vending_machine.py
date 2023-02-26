import sys

def check_text(price):
    if type(price) is str and not price.isdecimal():
        print('整数を入力してください');
        sys.exit();
    elif type(price) is int and price < 0:
        print('金額が不足しています');
        sys.exit();

input_price = input('input:');
check_text(input_price);

product_price = input('product:');
check_text(product_price);

change = int(input_price) - int(product_price);
check_text(change);

coin = [5000, 1000, 500, 100, 50, 10, 5, 1];

for i in coin:
    r = change // i;
    change %= i;
    print(str(i) + ':' + str(r));

