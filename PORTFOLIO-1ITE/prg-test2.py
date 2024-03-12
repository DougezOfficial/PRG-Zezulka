s = ["A", "B", "C"]

s[0], s[-1] = s[-1], s[0]

print(s[1])

if s[0] == "A":
    print("ano")
else:
    print("ne")

for x in s:
    print("-{}-".format(x))