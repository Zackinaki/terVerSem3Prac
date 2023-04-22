# Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый 
# месяц равна 0.1, для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый 
# месяц выйдут из строя: а). все детали б). только две детали в). хотя бы одна деталь г). от одной 
# до двух деталей?

import numpy as np
import pandas as pd
from math import factorial as fl

p1=0.1
p2=0.2
p3=0.25
n=3
k=1

pA=(p1*p2*p3)*100
print(f'что в первый месяц выйдут из строя: а). все детали = {pA :.2f}%')

pATolkDvedet=p1*p2*(1-p3)+p1*p3*(1-p2)+(1-p1)*p2*p3
print(f'что в первый месяц выйдут из строя: б). только две детали = {pATolkDvedet*100 :.2f}%')

pAHotOdn=(1-(1-p1)*(1-p2)*(1-p3))*100
print(f'что в первый месяц выйдут из строя: в). хотя бы одна деталь = {pAHotOdn :.2f}%')

pAOtOdnDoDvuh=p1*(1-p2)*(1-p3)+(1-p1)*p2*(1-p3)+(1-p1)*(1-p2)*p3+pATolkDvedet
print(f'что в первый месяц выйдут из строя: г). от одной до двух деталей = {pAOtOdnDoDvuh*100 :.2f}%')

