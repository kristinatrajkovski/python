def is_prime(n):
    t=2
    l=[]
    while (t<=n):
        m=0
        for i in l:
            if t%i==0:
                m=m+1
                break

        if m==0:
            l.append(t)
        
        t=t+1
    
    if (n>1):
        if (l[len(l)-1]==n):
            return True
        else:
            return False
    else: 
        return False

