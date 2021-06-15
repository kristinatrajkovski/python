
i=10000
l=[]
while i<100000:
    if (((i-1)%6==0) or ((i+1)%6==0)) and (i%5!=0):
        if(i//10000==i%10) and ((i//1000)%10==(i%100)//10):
             l.append(i)
            
    i=i+1
print(l)