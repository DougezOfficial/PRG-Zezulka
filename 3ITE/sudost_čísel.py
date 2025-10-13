# tato funkce zkontroluje jestli je číslo prvočíslo
def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    for i in range(2, int(cislo**0.5) + 1):
        if cislo % i == 0:
            return False
    return True

cislo = int(input("Zadej číslo: "))
if je_prvocislo(cislo):
    print(f"{cislo} je prvočíslo.")
else:
    print(f"{cislo} není prvočíslo.") 

#zkontroluje jestli je číslo vetší než 0
if cislo <=  0:
    print("Zadej číslo větší než 0")
    exit()

#proměnné
sudé = 0
liché = 0
prvočísla = 0

#projde čísla od 1 do zadaného čísla
for i in range(1, cislo + 1):
    if i % 2 == 0:
        sudé += 1
    else:
        liché += 1

    #zkontroluje jestli je číslo dělitelné 3
    if i % 3 == 0:
        print(f"{i} je dělitelné 3")
    else:
        print(f"{i} není dělitelné 3")

    #kontrola prvočísel
    je_prvo = je_prvocislo(i)
    if je_prvo:
        prvočísla += 1
    
    #napíše info o čísle
    print(f"Číslo {i} je {'sudé' if i % 2 == 0 else 'liché'} a {'je' if je_prvocislo(i) else 'není'} prvočíslo.")

#souhrn
print("\n      --- Souhrn ---\n")
print(f"Celkem sudých čísel: {sudé}") 
print("\n--- --- --- --- --- --- ---\n")
print(f"Celkem lichých čísel: {liché}")
print("\n--- --- --- --- --- --- ---\n")
print(f"Celkem prvočísel: {prvočísla}")
print("\n--- --- --- --- --- --- ---\n")



