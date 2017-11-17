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

#===========================================================================================================================
#"main()"

conteudoFormatado = abreInst()
print(conteudoFormatado)
