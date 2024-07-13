# cook your dish here
for i in range(int(input())):
    x, y, z, a = map(int, input().split())
    if (x == y == z == a == 0):
        print("IN")
    else:
        print("OUT")
