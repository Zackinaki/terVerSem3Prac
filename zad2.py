# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из 
# которых 5 белых. Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. 
# Какова вероятность того, что 3 мяча белые?

import numpy as np
import pandas as pd
from math import factorial as fl

def combination(n,k):
    return(fl(n)/(fl(k)*(fl(n-k))))

n1=8
b1=5
n2=12
b2=5
k1=2
k2=4
k3=3

p1DvaBel=(combination(b1,k1)/combination(n1,k1))

p2OdinBel=combination(b2,k3-k1)*combination(n2-b2,(k2+k1)-k3)/combination(n2,k2)

p3Bel1=p1DvaBel*p2OdinBel

p1OdinBel=combination(b1,k1-1)*combination(n1-b1,1)/combination(n1,k1)
p2DvaBel=combination(b2,2)*combination(n2-b2,2)/combination(n2,k2)
p3Bell2=p1OdinBel*p2DvaBel

p1NolBel=combination(b1,0)*combination(n1-b1,2)/combination(n1,k1)
p2TriBel=combination(b2,3)*combination(n2-b2,1)/combination(n2,k2)

p3Bel3=p1NolBel*p2TriBel

pObsh=(p3Bel1+p3Bell2+p3Bel3)*100
print(f'вероятность того, что 3 мяча белые = {pObsh :.2f}%')