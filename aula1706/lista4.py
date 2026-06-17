#Descobrindo o tamanho da lista
nomes = ["Jecíca", "Ronaldo", "Silmara", "João", "Sarah"]

print(len(nomes))

# Saber se existe um elemanto na lista
if "Jecíca" in nomes:
    print("Está na lista")
else:
    print("Não está na lista")

# A posição de um elemento na lista
indice = nomes.index("Ronaldo")
print(f" O Ronaldo está no índice {indice}")

#Percorrer a lista 
for nome in nomes:
    print(nome)

#Percorrer a lista com índice e valor
for name, nome in enumerate(nomes):
    print(name, nome)

#Linpar toda a lista
nomes. clear()
print(nomes)