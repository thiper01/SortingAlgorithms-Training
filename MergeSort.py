def Intercala(p,q,n,v):
    w=[0]*(n-p) #tamanho do vetor w eh igual n-p
    k=0 #indice do vetor w
    i=p #indice do 1o subvetor
    j=q #indice do 2o subvetor
    while i<q and j<n:
        if v[i] < v[j]:
            w[k]=v[i]
            i+=1
        else:
            w[k]=v[j]
            j+=1
        k+=1
    #testa se sobrou elementos nos subvetores
    while i<q :
        w[k]=v[i]
        i+=1
        k+=1
    while j<n :
        w[k]=v[j]
        j+=1
        k+=1
    #copia o vetor w[] para v[]
    i=p
    k=0
    while i<n:
        v[i]=w[k]
        i+=1
        k+=1


def MergeSort(p, n, v):

    if p < n-1: # so faz as chamadas recursivas se tivermos um vetor
                # com tamanho maior que 1
        q=(p + n)//2 #divisao inteira, q eh o meio do vetor
        MergeSort(p,q,v) #chamada a esquerda
        MergeSort(q,n,v) #chamada a direita
        Intercala(p,q,n,v)

#----MAIN------
#Teste da intercalacao
#v=[1,3,5,6,2,4,7,8]
#Intercala(0,4,len(v),v)


# para o MergeSort é passado o indice do primeiro elemento,
# o tamanho do vetor  e o vetor propriamente
v=[1, 4, 8, 3, 6, 5, 2, 7]
print("Vetor original: ", v)
MergeSort(0,len(v),v)
print(v)
