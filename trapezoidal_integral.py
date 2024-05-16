
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi,sin, sqrt,exp
def trapexoidal_integral(f,a=0,b=1,N=100):
    h=b-a/N
    s=0 #面積s
    for k in range(1,N+1):
        s_k=h/2*((a+(k-1)*h)+(a+k*h)) #s_K=K番目の時の面積
        s=s+s_k
    return (s)

#問1
def f1(x):
    return sin 

print(trapexoidal_integral(f1,N=50))
#問2
def f2(x):
    return 4/(1+x**2)
print(trapexoidal_integral(f2))

#問3
def f3(x):
    return sqrt(pi)*exp(-x**2)
print(trapexoidal_integral(f3,-100,100,1000))


