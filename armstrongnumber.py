num=int(input("enter the number"))
original=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if(original==sum):
    print("armstrong")
else:
    print("not armstrong")
    

