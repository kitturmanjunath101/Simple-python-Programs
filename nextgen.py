# cook your dish here
for i in range(int(input())):
    x,y,a,b=map(int,input().split())
    if((x*y<=(a*b))):
        print("yes")
    else:
        print("no")