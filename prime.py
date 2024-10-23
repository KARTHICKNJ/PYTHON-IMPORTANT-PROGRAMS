'''n=int(input("Enter a Number:"))
if(n==1):
    print(n,"is not a prime number")
if(n>100):
    for i in range(100,201):
        if(n%2==0):
            print(i)
            print(n,"is not a prime number")
            break
    else:
        print(n,"is prime number")'''
        
#range
a=100
b=200
for i in range(a,b):
    if(i%2==0):
        continue
    else:
        print(i)
