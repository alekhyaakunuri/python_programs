s=input()
m_count=0
f_count=0
l=list(s)
for i in range(len(l)):
    if(l[i]=='M' or l[i]=='m'):
        m_count+=1
        
for j in range(len(l)):
    if(l[j]=='F'or l[j]=='f'):
        f_count+=1
        
dictonery={'m_count':m_count,'f_count':f_count}
print(dictonery)
for i in range(len(l)):
    if(l[i]=='M' or l[i]=='m'):
        print(l[i],end='')
for j in range(len(l)):
    if(l[j]=='F' or l[j]=='f'):
        print(l[j],end='')

        
    