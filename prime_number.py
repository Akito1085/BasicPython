a = int(input("aの値を入力: "))
judge=True
if a==1:
    judge=False
else:
    for i in range(2,a):
        print(i)
        if a%i==0:
            judge=False
        
        
if judge==False:
    print("素数ではない")
else:
    print("素数である")



# TODO
##素数:1とその数以外で割り切れない整数　2~N-1の値で割って、割り切れない場合(常に余りが0以上の場合)＝素数
##2~N-1の値で割って、割り切れない場合(常に余りが0以上の場合)＝素数
##0%2,60%3,.....で余りが0になった場合、繰り返しをやめて、素数ではないと判定
##一度でも余りが0になった場合、判定が変わる。