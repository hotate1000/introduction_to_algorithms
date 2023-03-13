import os

print(os.listdir('/'));

for i in os.listdir('/'):
    # print(i + ' : ' + str(os.path.isdir('/' + i)));
    # print(i + ' : ' + str(os.path.isfile('/' + i)));
    if os.path.isdir('/' + i):
        print('dir：' + i);
    if os.path.isfile('/' + i):
        print('file：' + i);