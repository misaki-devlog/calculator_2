print("累積代入の計算ができます")
num_1=float(input('一つ目の数字を入力してください: '))
num_2=float(input('二つ目の数字を入力してください: '))
print('足し算')
a=num_1
a+=num_2
print(a)
print('引き算')
b=num_1
b-=num_2
print(b)
print('掛け算')
c=num_1
c*=num_2
print(c)
print('割り算')
d=num_1
d/=num_2
print(d)
print('べき乗（累乗）')
e=num_1
e**=num_2
print(e)
print('余りの計算')
f=num_1
f%=num_2
print(f)
input('Enterを押すと終了します')