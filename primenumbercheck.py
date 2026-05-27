num = int(input("Enter number: "))

isPrime = True
for i in range(2, num):

    if num % i == 0:
        isPrime = False
        break

if isPrime:
    print("Prime")
else:
    print("Not Prime")
