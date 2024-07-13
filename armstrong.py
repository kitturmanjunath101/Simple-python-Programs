# sum of cubes of its digits == armstrong
num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
print(sum)
if sum==num:
    print(sum,"this is armstrong number")
else:
    print("this is not armstrong number")