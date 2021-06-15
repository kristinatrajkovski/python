def primes_below(n):
    i=2
    l=[]
    while i<n:
        if (i==2) or (i==3) or (i==5):
            l.append(i)

        elif (((i-1)%6==0) or ((i+1)%6==0)) and (i%5!=0):
            l.append(i)
        
        i=i+1
    
    return l
