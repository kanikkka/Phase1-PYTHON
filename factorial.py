num=int(input("enter the number"))
for i in range(1,num+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
        print("factorial of",i,"is",fact)
        
