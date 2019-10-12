import random
import pandas as pd
a=random.randint(0,10)
print(a)
zongbiao=[]
for k in range(1000):
    people=[]
    for i in range(5):
        fenshu=random.randint(0,10)
        people.append(fenshu)
    zongbiao.append(people)
zongbiao=pd.DataFrame(zongbiao)
zongbiao.to_csv('zongbiao.txt',index=None,header=None,sep=' ')
