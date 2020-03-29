f = open("input.txt")

n = int(f.readline())

stari = f.readline().split()

stare_initiala = f.readline().strip()

stari_finale = f.readline().split()

alfabet = f.readline().split()

lista_muchii = []

muchii = f.readlines()

for muchie in muchii:

    m = muchie.split()

    lista_muchii.append(m)


f.close()


cuvant = input("Cuvantul dat este: ")

stare_curenta = stare_initiala

ok = 0



if cuvant == '':

    if stare_initiala in stari_finale:

        print("Cuvantul este acceptat")

    else:

        print("Cuvantul nu este acceptat")

else:

    for i in cuvant:
        for j in range(len(lista_muchii)):
            ok=0

            if lista_muchii[j][0] == stare_curenta and lista_muchii[j][1] == i:

                stare_curenta = lista_muchii[j][2]

                ok = 1

                break





    if ok == 0:

        print("Cuvantul nu este acceptat")

    elif ok == 1 and stare_curenta not in stari_finale:

        print("Cuvantul nu este acceptat")

    else:

        print("Cuvantul este acceptat")