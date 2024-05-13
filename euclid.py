a_list=[10,14,91]
b_list=[20,91,14]

for a,b in zip(a_list,b_list):

    if a>b:
        while True:
            if a%b==0:
                break
            else:
                a,b=b,a%b
        print(b)
    elif a==b:
        print(a)
    else:
        while True:
            if b%a==0:
                break
            else:
                b,a=a,b%a
        print(a)
    
# TODO
#aとbの最大公約数　a=bq+r r=a%b q=a//b , bの値をaに代入、a%bをbに代入するのを繰り返す。rが0になった時にやめる#