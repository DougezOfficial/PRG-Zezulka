import random

w, h, mines = 10, 5, 40

# gene field
field = [[0 for y in range(h)] for x in range(w)]

# put mine on random position
for i in range(mines):
    rx = random.randint(0, w - 1)
    ry = random.randint(0, h - 1)
    field[rx][ry] = "M"
    
# print field
for y in range(h):
    for x in range(w):
        print(field[rx][ry], end="")
    print()