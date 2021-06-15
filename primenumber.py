def is_prime(n):
    if n>1:
        if (n==2) or (n==3) or (n==5):
            return True
        elif (((n+1)%6==0) or ((n-1)%6==0)) and (n%5!=0):
            return True
        else:
            return False
    else:
        return False


