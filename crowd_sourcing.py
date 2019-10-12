import numpy as np
import pandas as pd
import random
weg=np.zeros([100,100])
knownet=pd.read_csv('knowledge_net.txt',sep=' ',header=None,index_col=None)
print(len(knownet))
xuesheng_net=pd.read_csv('zongbiao.txt',sep=' ',header=None,index_col=None)
v1=[]
v2=[]
for i in range(110):
    if i <10 or i %10==8 or i%10==9:
        v2.append(i)
    else:
        v1.append(i)
wv1=np.zeros([3,100])
def qiu_v(xuesheng_net):
    v=[]
    for i in range(1000):
        maxx=0
        for k in range(5):
           if xuesheng_net.iloc[i, k] > 6:
               maxx += 1
        v.append(maxx)
    return v
def time_refresh(xuesheng_net,time_list,v):
    for i in range(1000):
        suum = 0
        for k in range(5):
            suum += xuesheng_net.iloc[i, k]
        suum = suum / 5
        maax=v[i]
        time_list[i] = time_list[i] + 0.1 * 5 + 0.1 * suum + 0.1 * maax
        v.append(maax)
    return time_list
def wvr(i,time_list):
    # 返回值：列表wvr[100]和时间序列[1000]
    hei=0
    for j in range(i*10,(i+1)*10):
        haha=random.randint(0,10)
        haha1=time_list[j]
        hei+=haha*haha1
    return hei
v=qiu_v(xuesheng_net)
print(len(v))
timelist=np.zeros([1000])
for i in range(100):
    wv1[0,i]=i//10
timelist=time_refresh(xuesheng_net,timelist,v)
for i in range(100):
    wv1[1,i]=wv1[0,i]*0.5+0.1*wvr(i,timelist)
timelist=time_refresh(xuesheng_net,timelist,v)
for i in range(100):
    wv1[2,i]=wv1[1,i]*0.3+0.05*wvr(i,timelist)
print(wv1[2,99],wv1[1,99],wv1[0,99])
for i in range(350):
    if knownet.iloc[i,2]>10:
        u1=knownet.iloc[i,0]-10
        u2=knownet.iloc[i,2]-10
        weg[u1,u2]=1
        weg[u2,u1]=1
for i in range(100):
    for j in range(100):
        maxx=0
        maax=0
        for k in range(i*10,(i+1)*10):
            maxx+=v[k]
        for k in range(j*10,(j+1)*10):
            maax+=v[k]
        weg[i,j]=weg[i,j]*((wv1[2,i]+5+0.1*maxx)+(wv1[2,j]+5+0.1*maax))*0.5
finilly_data=[]
node=list(range(110))
edge=list(knownet)
wv=list(wv1)
we=list(weg)
finilly_data.append(node)
finilly_data.append(edge)
finilly_data.append(wv)
finilly_data.append(we)




