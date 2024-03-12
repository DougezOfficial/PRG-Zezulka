import math
def o(r):
    return round(2 * math.pi * r, 3)
print (o(10))

def s(r):
    return math.pi * r ** 2
print(s(10))

money = 0.01
for day in range(1, 31):
    print(str(day) + "\t" + str(money))
    money*=2