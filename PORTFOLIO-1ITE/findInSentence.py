

f = open("sentence.txt", "r")


sentence = f.read()
#sentence = input("Zadej větu: ")
char = input("Zadej hledané slovo")
#char = input("Zadej hledaný znak: ")
count = 0


for x in sentence:
    if x == char:
        count += 1

#print(count)
print(sentence, count)