a_list=[10,14,91]
b_list=[20,91,14]

a=int(input("enter"))
b=int(input("number"))

def euclid(a,b):
    if a>b:
        while True:
            if a%b==0:
                break
            else:
                a,b=b,a%b
        return b
    elif a==b:
        return a
    else:
        while True:
            if b%a==0:
                break
            else:
                b,a=a,b%a
        return a
print("問1の答え",euclid(a,b)) 

#問2
def coprime(a,b):
    return euclid(a,b)==1

print("問2の答え",coprime(a,b))

