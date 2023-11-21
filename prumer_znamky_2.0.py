znamky = [[3,1], [3,2], [3,1], [10,3], [4,4]]
prvni_cisla = []
prm = []
pocet = len(znamky)
for z in znamky:
    prvni_cisla.append(z[0])

for y in znamky:
    prm.append(y[1])

pocet_vah = sum(prvni_cisla)

nasobek = [x * y for x, y in znamky]
nasobek = sum(nasobek)

prm = sum(prm)
prm = prm / pocet

prumer = nasobek / pocet_vah
prumer = round(prumer, 2)

print("Průměr s vahami je :",prumer)
print("Průměr bez bah je :",prm)