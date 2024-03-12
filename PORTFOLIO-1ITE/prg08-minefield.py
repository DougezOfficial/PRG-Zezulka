import random


print("Minefield")

w = 10
h = 5
mine_cnt = 5
#gene with zero
field = [[0 for i in range(h)]for j in range(w)]

if mine_cnt > w * h:
    mine_cnt = 0
    print("Too many mines.")
for i in range(mine_cnt):
    while True:
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break