#number palindrome
num=int(input("Enter a number:"))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if(rev==num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
    
#string
str=input("Enter a string:")
rev=""
for i in str:
    rev=rev+i
if(rev==str):
    print(str,"it is plaindrome")
else:
    print(str,("is not a palindrome"))