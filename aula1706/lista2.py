compras = ["Maçã", "Carne", "Macarrão", "Pão", "Molho"]
for compra in compras:
    print(compra)

compras[1] = "carne"
print(compra)
#Acrescente mais dois elementos 
#Substitua os elementos de índice 3 e 5

compras.append("Ovos")
print(compras)
compras.append("Uva")
print(compras)

compras[3] = "Salsicha"
print(compras)
compras[5] = "Azeitona"
print(compras)