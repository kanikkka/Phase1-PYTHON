num=int(input("enter the first number"))
num1=int(input("enter the second number "))
num2=int(input("enter the third number"))
if num>num1 and num>num2:
    print(num,"is largest ")
elif num1>num and num1>num2:
    print(num1,"is largest")
else:
    print(num2,"is largest")