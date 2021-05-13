import json

def PreguntarNumero(numero):
    """ funcion que pregunta el numero favorito del usuario"""
    filename =  'favorito.json'
    with open(filename,'w') as f:
        json.dump(numero,f)

def MostrarNumero():
    """ funcion que muestra el numero"""
    filename = 'favorito.json'
    with open(filename) as f:
        numero = json.load(f)
        print(f"Tu numero favorito es {numero}\n")