for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()[:n]))
    count=0
    for i in l:
        if(i>=1000):
            count+=1
    print(count)