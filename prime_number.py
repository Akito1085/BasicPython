
def prime_number(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False     
        return True


n =int(input("nの値を入力: "))
print(prime_number(n)) 


