import pandas as pd
nm=[]
for i in range(10):
    for j in range((i+1)*10,(i+1)*10+3):
        if j %10==0:
            nm.append([j,i,i])
        for k in range(j+1,(i+2)*10):
            b=[j,i,k]
            nm.append(b)
    for j in range((i+1)*10+3,(i+2)*10-2):
        for k in range(j+1,(i+2)*10-2):
            b=[j,i,k]
            nm.append(b)
knownet=pd.DataFrame(nm)
knownet.to_csv('knowledge_net.txt',index=None,sep=' ',header=None)