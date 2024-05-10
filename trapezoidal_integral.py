from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi
a=sin(0)
b=sin(pi/2)
N=100
h=b-a/N
s=0 #面積s
for k in range(1,N+1):
    print(k)
    s_k=h/2*((a+(k-1)*h)+(a+k*h)) #s_K=K番目の時の面積
    s=s+s_k
print(s)



