def processa_lista(valores):
    pares = []
    impares = []

    for valor in valores:
        if valor == 0:
            break

        if valor % 2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
    
    for i, par in enumerate(pares):
        pares[i % 5] = par
    pares = pares[:5]

    for i, impar in enumerate(impares):
        impares[i % 5] = impar
    impares = impares[:5]
    
    return pares, impares

def indice_menor(lista):
    pass

def organizar_alturas(lista):
    lista = sorted(lista[:-1])
    lista_ordenada = []
    lista_ordenada.append(lista[0])
    lista_ordenada.append(lista[2])
    lista_ordenada.append(lista[3])
    lista_ordenada.append(lista[1])
    return lista_ordenada

def ler_valores():
    valores = []

    while True:
        valor = float(input('Digite um valor: '))
        valores.append(valor)
        if valor == 0:
            break

    return valores

def formatar_alturas(lista):
    for i, altura in enumerate(lista):
        lista[i] = f'{altura:.2f}'
    return lista

def intercalar_listas(lista1, lista2):
    lista = lista1 + lista2
    lista.sort()
    return lista

def lista_maior18(pessoas):
    pessoas_maiores = []

    for pessoa in pessoas:
        idade = pessoas[pessoa]
        if idade > 18:
            pessoas_maiores.append(pessoa)

    pessoas_maiores.sort()
    return pessoas_maiores

def q1(pessoas = {"Joao": 25, "Maria": 10}):
    resultado = lista_maior18(pessoas)
    return resultado

def q2(lista1 = [1, 3, 5], lista2 = [2, 4, 6, 8, 10]):
    resultado_intercalado = intercalar_listas(lista1, lista2)
    return resultado_intercalado

def q3(valores = None):
    # valores = ler_valores()
    pares, impares = processa_lista(valores)
    return pares, impares

def q4(valores = None):
    # valores = ler_valores()
    lista_ambrosina = organizar_alturas(valores)
    return formatar_alturas(lista_ambrosina)


# print(q1())
# print(q2())
# print(q3())
# print(q4())




def main():
    pass

if __name__ == "__main__":
    main()


