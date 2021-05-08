def capitales(ciudad,capital):
    enunciado = f"la capital de {ciudad} es {capital}"
    return enunciado.title()

print(capitales('monterrey','nuevo leon'))


# alimentando una funcion con un numero indeterminado de argumentos para crear un diccionario
def makeSandwich(TipoDePan,Proteina,**sandwich):
    sandwich ['TipoDePan'] = TipoDePan
    sandwich ['Proteina'] = Proteina
    return sandwich
pedido = makeSandwich('de avena','jamon', verdura = 'jitomate',
                      aderezo = 'miel y mostaza')

print(pedido)
