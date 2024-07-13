num=int(input("enter a number:"))
factorial=1
if num<0:
    print("the factorial of this number doesnt exists")
elif num==0:
    print("the factorial of this number is 0")
else:
    for i in range (1,num+1):
        factorial=factorial*i
    print("the factorail of",num,"is:",factorial)