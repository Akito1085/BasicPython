a=int(input("正の整数を記入"))
b=int(input("正の整数を記入"))

def euclid(a,b):
    if b<a:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
       
print("問1の答え",euclid(a,b)) 

#問2
def coprime(a,b):
    return euclid(a,b)==1

print("問2の答え",coprime(a,b))


