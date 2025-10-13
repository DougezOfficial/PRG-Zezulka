#Tahle funkce vypočítá BMI podle výšky a váhy
def výpočet_bmi(váha, výška):
    bmi = váha / (výška ** 2)
    return bmi

#tahle funkce určí kategorii BMI
def kat(bmi):
    if bmi < 18.5:
        return "Podváha"
    elif 18.5 <= bmi < 24.9:
        return "Normální váha"
    elif 25 <= bmi < 29.9:
        return "Nadváha"
    else:
        return "Obezita"
    
výška = float(input("Zadej svou výšku v metrech (např. 1.75): "))
váha = float(input("Zadej svou váhu v kilogramech (např. 70): "))   

bmi = výpočet_bmi(váha, výška)
kategorie = kat(bmi)

#vypíše v přehledným formátu
print(f"Tvoje BMI je: {bmi:.2f}, což znamená, že máš: {kategorie}")
