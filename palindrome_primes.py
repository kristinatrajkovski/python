l=[2]
t=2
p=[]
while (t<100000):
    m=0
    for i in l:
        if t%i==0:
            m=m+1
            break 

    if (m==0):
        l.append(t)
        if (t>10000) and (t//10000==t%10) and ((t//1000)%10==(t%100)//10):
            p.append(t)
    t=t+1

print(p)

