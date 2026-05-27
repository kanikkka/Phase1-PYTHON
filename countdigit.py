num=int(input("enter the number"))
original=num
count=0
for i in range(len(str(num))):
    num=num//10
    count=count+1
    print(count)
