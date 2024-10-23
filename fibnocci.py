n=int(input())
a=0
b=1
if n==0:
    print(b)
else:
    for i in range(0,n):
        c=a+b
        a=b
        b=c
    print(c)