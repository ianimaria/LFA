
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

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

tabel = [ ['gol']*i for i in range(n)]

# stari separabile prin cuvantul lambda

if stari[0] in stari_finale and stari[1] not in stari_finale:
    tabel[1][0]= 'lambda'

for i in range(1,len(tabel)):
    for j in range(i):
        if stari[i] in stari_finale and stari[j] not in stari_finale:
            tabel[i][j]= 'lambda'
        elif stari[i] not in stari_finale and stari[j] in stari_finale:
            tabel[i][j]= 'lambda'

mult=[]

# cautam cuvinte de lungime 1

for i in alfabet:
    for j in range(len(lista_muchii)):
        if lista_muchii[j][1]==i and lista_muchii[j][2] in stari_finale:
            mult.append(lista_muchii[j][0])
    
   
    if mult != []:
        for k in stari:
            if k not in mult:
                for l in mult:
                    
                    if stari.index(k) > stari.index(l) and tabel[stari.index(k)][stari.index(l)] == 'gol' :
                        tabel[stari.index(k)][stari.index(l)] = i
                    
                    elif stari.index(l) > stari.index(k) and tabel[stari.index(l)][stari.index(k)] == 'gol' :
                        tabel[stari.index(l)][stari.index(k)] = i
    mult=[]

   
# cautam cuvinte de lungime 2


for i in range(1,len(tabel)):
    for j in range(i):

        if tabel[i][j] == 'gol' :
           
            for a in alfabet:
               
               for k in range(len(lista_muchii)-1,-1,-1):
                   
                   if lista_muchii[k][0] == stari[i] and lista_muchii[k][1] == a:
                       x = stari.index(lista_muchii[k][2])
                       
                   if lista_muchii[k][0] == stari[j] and lista_muchii[k][1] == a:
                       y = stari.index(lista_muchii[k][2])
                  

               if x > y and tabel[x][y] in alfabet:
                 tabel[i][j] = a + tabel[x][y] 
                 break
                
               
               elif x < y and tabel[y][x] in alfabet:
                   tabel[i][j] = a + tabel[y][x]
                   break

               else:
                   tabel[i][j] = 'echiv'
                
Q=[]
I=[]
F=[]
M=[]         

for j in range(len(stari)):
    c = stari[j]
    for i in range(1,len(stari)):
        if i != j and i>j and tabel[i][j] == 'echiv':
            c += stari[i]
    ok = 1        
    for k in range(len(Q)):
         if c in Q[k]:
            ok=0
    
    if ok==1:
        Q.append(c)

for i in range(len(stari_finale)):
    for j in range(len(Q)):
        if stari_finale[i] in Q[j] and Q[j] not in F:
            F.append(Q[j])
        if I == []:
            for k in Q[j]:
                if k in stare_initiala and I==[]:
                    I.append(Q[j])
                  


for i in range(len(Q)):
    for j in range(len(lista_muchii)):
        if lista_muchii[j][0] in Q[i]:
            for k in range(len(Q)):
                if lista_muchii[j][2] in Q[k] and [Q[i], lista_muchii[j][1], Q[k]] not in M:
                    M.append([Q[i], lista_muchii[j][1], Q[k]])

print('Q =',Q)
print('I =',I)
print('F =',F)
print('M =',M)                

G = nx.MultiDiGraph()

G.add_nodes_from(Q)

color_map=[]

for node in G:
    if node in I and node not in F:
        color_map.append('darkgrey')
    elif node in F and node in I:
        color_map.append('lightyellow')
    elif node in F and node not in I:
        color_map.append('lightseagreen')
    else:
        color_map.append('skyblue')

print(color_map)
labels={}
shape=[]
edgecolors=[]

for i in M:
    G.add_edge(i[0],i[2])

    labels[i[0],i[2]]=i[1]



for i in range(len(Q)):
    ok=0
    k=0
    for j in range(len(M)):

        if Q[i] == M[j][0] and Q[i] == M[j][2] and k==0:
             edgecolors.append('red')
             ok=1
             k=1
    if ok==0:
        edgecolors.append('black')
    

pos = nx.circular_layout(G)

nx.draw(G,pos,node_color = color_map, node_size = 2500, edgecolors = edgecolors, linewidths = 2, with_labels = True)
nx.draw_networkx_edge_labels(G,pos, edge_labels = labels ,font_color='midnightblue')

plt.show()