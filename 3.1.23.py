import random
vardi = ["viens", "divi", "trīs", "četri"]

while True:
    vards = random.choice(vardi)
    minetaisVards = list("_" for _ in vards)
    dzivibas = 5



    while dzivibas > 0 and not "".join(minetaisVards)== vards:
        inp = input("Ievade: ")
        inp = inp[0]
        # TODO: garuma pārbaude

        uzminets = False
        for iii in range(0, len(vards)):
            if vards[iii] == inp:
                minetaisVards[iii] =inp
                uzminets = True

        if uzminets == False:
            dzivibas -= 1

        print(f"dzivibas: {dzivibas}")
        print("".join(minetaisVards))

    if dzivibas == 0:
        print("Tu zaudēji")
    else:
        print("Tu uzvarēji")

    if not input("Vai turpināt? j/n")[0].lower() == "j":
        break