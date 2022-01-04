def f(n,a,b):
    print(n,a,b)
    if n==0:
        return b+1
    elif n==1 and b==0:
        return a
    elif n==1:
        return a+b
    elif n==2 and b==0:
        return 0
    elif n==2:
        return a*b
    elif n>=3 and b==0:
        return 1
    elif n==3:
        return a**b
    else:
        return f(n-1,a,f(n,a,b-1))
print(f(4,4,4))
