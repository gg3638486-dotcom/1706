 #Criar uma lista de números, com 5 elementos.
#Mostra a lista
#Inserir dois elementos no final da lista
#Inserir u elemento no final da lista
#Inserir um elementos na posição 3 e outra na posição 1

números = [6, 38, 73, 20, 49]
for número in números:
    print(número)

números.append(93)
print(números)

números.append(54)
print(números)

números.insert(2, 14)
print(números)

números.insert(0, 80)
print(números)