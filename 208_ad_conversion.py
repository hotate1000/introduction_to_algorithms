meiji=1868
taisho=1912
showa=1926
heisei=1989
reiwa=2019

def ad_conversion(n):
    if n > reiwa:
        return f'令和：{str(n - reiwa + 1)}年';
    elif n > heisei:
        return f'平成：{str(n - heisei + 1)}年';
    elif n > showa:
        return f'昭和：{str(n - showa + 1)}年';
    elif n > taisho:
        return f'大正：{str(n - taisho + 1)}年';
    elif n >= meiji:
        return f'明治：{str(n - meiji + 1)}年';
    else:
        return f'西暦{n}年は令和、平成、昭和、大正、明治以外の年号となります。';

print(ad_conversion(1868));
print(ad_conversion(1869));
print(ad_conversion(1867));
print(ad_conversion(1915));
print(ad_conversion(1929));
print(ad_conversion(1992));
print(ad_conversion(2022));