for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()