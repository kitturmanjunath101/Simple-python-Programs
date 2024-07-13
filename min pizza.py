
for i in range(int(input())):
    x, y = map(int, input().split())
    pizza = (x * y) // 4
    if ((x * y) % 4 == 0):
        print(pizza)
    else:
        print(pizza + 1)
