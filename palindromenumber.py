num=int(input("enter the number"))
rev=0
original=num
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
    
if(original==rev):
        print("pallindrome")
else:
        print("not pallindrome")