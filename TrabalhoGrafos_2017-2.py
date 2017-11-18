"""abreInst() - Função pede o nome do arquivo de entrada para o usuário,
                abre o arquivo e realiza a formatação do conteúdo do arquivo
                e retorna este conteúdo como uma lista de números."""
def abreInst():
    nome=input("Informe o nome da instância: ")         #interação com o usuário
    with open(nome) as inst:                            #abre arquivo como inst
        conteudo = inst.read()                          #salva o conteudo do arquivo
    conteudo = conteudo.replace('\n',' ').split(' ')    #substitui os '/n' por espaços e divide o conteudo em uma lista
    conteudo.remove('')                                 #remove um char vazio do fim da lista (gambiarra)

    for x in range(len(conteudo)):                      
        conteudo[x] = int(conteudo[x])                  #laço que tranforma as strings da lista em inteiros
    return conteudo                                     #retorta lista

#===========================================================================================================================
"""geraArestas() - Função auxiliar para a função geraGrafo(),
                   essa função organiza as arestas e pesos 3 a 3 em uma lista de listas"""
def geraArestas(arestas):
    arestAux = []
    cont = len(arestas)/3                               #cont recebe a qtd de arestas e pesos
    for x in range(int(cont)):
        arestAux.append(arestas[x*3:x*3+3])             #arestAux recebe cada aresta e peso organizado 3 a 3
    return arestAux 
#===========================================================================================================================
"""geraGrafo - Função termina de formatar a entrada e gera um grafo das listas de adjacências de cada nodo,
               com seus respectivos pesos, sendo essas adjcências tanto do inicio para o fim quanto do fim para o inicio."""
def geraGrafo(arestasEpesos,mn):
    arestas = geraArestas(arestasEpesos)
    grafo=[[]]
    for x in range(mn[0]-1):                            #laço para criar os nodos dentro da lista grafo
        grafo.append([])

    for cont in range(len(arestas)):                    
        inicio = arestas[cont][0]                       #divisão das informações de cada aresta
        final = arestas[cont][1]
        peso = arestas[cont][2]

        grafo[inicio].append([final,peso])              #criação das adjacências partindo do inicio para o final da aresta
        grafo[final].append([inicio,peso])              #criação das adjacências partindo do final para o inicio da aresta
    return grafo
        
#===========================================================================================================================
#"main()"
conteudoFormatado = abreInst()
mn = conteudoFormatado[:2]
arestasEpesos = conteudoFormatado[2:]
grafo = geraGrafo(arestasEpesos,mn)

print(arestasEpesos)                                    #impressão do conteudo formatado do arquivo sem o mn
for nodo in grafo:
    print("nodo ",grafo.index(nodo),": ",nodo)          #impressão dos nodos do grafo finalizado
