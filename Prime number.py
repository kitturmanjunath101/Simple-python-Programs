num=int(input("enter a number"))
flag=False
if num==1:
    print("it is not prime number")
elif num>1:
    for i in range(2,num):
        if( num % i) == 0:
            flag=True
            break
    if flag:
        print(num," is not prime number")
    else:
        print(num,"is a prime number")


