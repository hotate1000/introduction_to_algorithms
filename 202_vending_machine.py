import sys

def confirmation_input_information(price):
    if not price.isdigit():
        print('整数を入力してください');
        sys.exit();

def check_integer(numbers):
    if numbers < 0:
        print('金額が不足しています');
        sys.exit();

input_price = input('insert: ');
confirmation_input_information(input_price);
product_price = input('product: ');
confirmation_input_information(product_price);
change = int(input_price) - int(product_price);
check_integer(change);

coin = [5000, 2000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i;
    change %= i;
    print(str(i) + ': ' + str(r));
