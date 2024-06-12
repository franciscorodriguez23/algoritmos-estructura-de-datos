def lista_inversa(lista):
    # si la lista está vacía no hace nada
    if not lista:
        return
    # llamada recursiva con la sublista excluye el primer elemento
    lista_inversa(lista[1:])
    # imprime el primer elemento de la lista actual
    print(lista[0])

mi_lista = [1,2,3,4,5,6,7,8,9,10]
lista_inversa(mi_lista)
