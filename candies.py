# cook your dish here
import math
for i in range(int(input())):
    x,y=map(int,input().split())
    if(x<=y):
        print(0)
    else:
        z=x-y
        b=z/4
        print(math.ceil(b))