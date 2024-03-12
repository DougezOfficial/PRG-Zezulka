start, end = (int(x) for x in input("Vlož dvě čísla oddělená mezerou: ").split())

current = start
while current <= end:
    print(current, end=" ")
    current += 1
print()