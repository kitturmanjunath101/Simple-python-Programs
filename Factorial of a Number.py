num=int(input("enter a number:"))
factorial=1
if num<0:
    print("factorial of this number doesnt exist")
elif num==0:
    print("factorial of 0 is number 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial of",num,"is",factorial)