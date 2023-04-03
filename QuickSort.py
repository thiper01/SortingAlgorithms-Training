def particao(v,p,r):
    c = v[p]
    i = p+1
    j = r
    while i <= j:
        #descarta da esquerda para direita os memores ou iguais o pivo
        if v[i] <= c:
            i+=1
        # descarta da direita para esquerda elementos maiores que o pivo
        elif v[j] > c:
            j-=1
        #achei um elemento maior que o pivo a esquerda e menor igual ao pivo a direita
        else:
            #troca os elementos de posicao
            temp = v[i]
            v[i]=v[j]
            v[j]=temp
            i+=1
            j-=1
        
        
    # posiciona o pivo c corretamenta
    v[p] = v[j]
    v[j] = c
            
    return j
#QuickSort
def QuickSort( v, p, r):

    if p < r :
        j = particao(v,p,r)
        #chama QuickSort recursivamente para esquerda do pivo
        QuickSort(v,p,j-1)
        #chama QuickSort recursivamente para direita do pivo
        QuickSort(v,j+1,r)
        

#----MAIN------
#Teste da particao
#v=[5,9,6,4,3]
v=[5, 9, 6, 4, 3]
print("Vetor Original: ", v)
QuickSort(v, 0, len(v)-1)

print(v)
