def to_hex(n):
    t1=n%16
    t2=n//16
    if (t1>9):
        if (t1==10):
            s2="a"
        elif (t1==11):
            s2="b"
        elif (t1==12):
            s2="c"
        elif (t1==13):
            s2="d"
        elif (t1==14):
            s2="e"
        elif (t1==15):
            s2="f"
    else:
        s2=str(t1)
    if (t2>9):
        if (t2==10):
            s1="a"
        elif (t2==11):
            s1="b"
        elif (t2==12):
            s1="c"
        elif (t2==13):
            s1="d"
        elif (t2==14):
            s1="e"
        elif (t2==15):
            s1="f"
    else:
        s1=str(t2)
    s=s1+s2
    return s

def hex_color (red, green, blue):
    r1=red%16
    r2=red//16
    if (r1>9):
        if (r1==10):
            rr2="a"
        elif (r1==11):
            rr2="b"
        elif (r1==12):
            rr2="c"
        elif (r1==13):
            rr2="d"
        elif (r1==14):
            rr2="e"
        elif (r1==15):
            rr2="f"
    else:
        rr2=str(r1)
    if (r2>9):
        if (r2==10):
            rr1="a"
        elif (r2==11):
            rr1="b"
        elif (r2==12):
            rr1="c"
        elif (r2==13):
            rr1="d"
        elif (r2==14):
            rr1="e"
        elif (r2==15):
            rr1="f"
    else:
        rr1=str(r2)
    r=rr1+rr2
    g1=green%16
    g2=green//16
    if (g1>9):
        if (g1==10):
            rg2="a"
        elif (g1==11):
            rg2="b"
        elif (g1==12):
            rg2="c"
        elif (g1==13):
            rg2="d"
        elif (g1==14):
            rg2="e"
        elif (g1==15):
            rg2="f"
    else:
        rg2=str(g1)
    if (g2>9):
        if (g2==10):
            rg1="a"
        elif (g2==11):
            rg1="b"
        elif (g2==12):
            rg1="c"
        elif (g2==13):
            rg1="d"
        elif (g2==14):
            rg1="e"
        elif (g2==15):
            rg1="f"
    else:
        rg1=str(g2)
    g=rg1+rg2
    b1=blue%16
    b2=blue//16
    if (b1>9):
        if (b1==10):
            rb2="a"
        elif (b1==11):
            rb2="b"
        elif (b1==12):
            rb2="c"
        elif (b1==13):
            rb2="d"
        elif (b1==14):
            rb2="e"
        elif (b1==15):
            rb2="f"
    else:
        rb2=str(b1)
    if (b2>9):
        if (b2==10):
            rb1="a"
        elif (b2==11):
            rb1="b"
        elif (b2==12):
            rb1="c"
        elif (b2==13):
            rb1="d"
        elif (b2==14):
            rb1="e"
        elif (b2==15):
            rb1="f"
    else:
        rb1=str(b2)
    b=rb1+rb2

    k="#"+r+g+b
    return k

