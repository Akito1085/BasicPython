def prime_number(n):
    judge=True
    for i in range(2,n):
        if n%i==0:
            judge=False
            
            
    return judge==True

n =int(input("nの値を入力: "))
if n>0:
    print(prime_number(n))
else:
    print("正の整数を入力してください")



# TODO

