from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

from math import pi
a=0 #区間a
b=pi/2 #区間b
N=100
h=(b-a)/N
s=0 #面積s
for k in range(1,N+1):
    s_k=h/2*(sin(a+(k-1)*h)+sin(a+k*h)) #s_K=K番目の時の面積
    s=s+s_k
print(s)



