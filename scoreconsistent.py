for i in range(int(input())):
    a,b=map(int,input().split())
    x,y=map(int,input().split())
    if ((x>=a) and (y>=b)):
        print("possible")
    else:
        print("impossible")

