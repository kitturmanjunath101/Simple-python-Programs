# cook your dish here
t=int(input())
for i in range(t):
    s = list(map(int, input().split()))
    print(s.sort())
    print(s[1])
