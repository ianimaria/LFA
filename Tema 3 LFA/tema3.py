
f = open("input.txt")

n= int(f.readline()) # lungimea max

N = [x.strip() for x in f.readline().split()] # lista cu neterminale

T = [x.strip() for x in f.readline().split()] # lista cu terminale

Start = f.readline().strip() 

p = [x.strip().split('->') for x in f.readlines()]

P={}

for i in range(len(p)):
    P.update({p[i][0]:(p[i][1].split(' | '))}) # dictionar cu productiile


def verificare_neterminale(word):
    for i in word:
        if i in N:
            return 0


def inlocuire(aux):

    for i in aux:
        if verificare_neterminale(i) == 0:
            for j in i:
                if j in N:
                    for k in P.get(j):
                        x = i
                        
                        if (k == "E"):
                            k=""
                        x = x.replace(j,k)

                        if len(x) <= 2*n:
                            aux.append(x)

        elif verificare_neterminale(i) != 0 and len(i) <=n and i not in finale:
            if i == "":
                finale.append("ε")
                aux.remove(i)
            else:
                finale.append(i)
    
    for word in aux:
        if verificare_neterminale(word) !=0 and len(word) <= n and word not in finale:
            if word == "":
                finale.append("ε")
                aux.remove(word)
            else:
                finale.append(word)
                aux.remove(word)      
   
aux = []

finale = []

for i in P[Start]:
    aux.append(i)

if n == 0:
    print("Nu se pot genera cuvinte de lungime 0")
else:
    inlocuire(aux)
    if finale:
        print("Cuvintele generate sunt: ", finale)
    else:
        print("Nu au fost generate cuvinte de lungime <= %s" %n)

