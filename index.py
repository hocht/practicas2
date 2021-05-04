
# Rodrigo Estilla Olvera
# Este es un comentario
# Tienes que ser mejor programador cada dia
bicicletas = ['benoto', 'calo', 'maseta', 'filtro']
print(bicicletas[0].title())
print(bicicletas[-1].upper())

mensaje = f"My first bicycle was a {bicicletas[-3].title()}."
print(mensaje)
bicicletas.append('campanolo')
mensaje = f"My first bicycle was a {bicicletas[-3].title()}."
print(mensaje)

# Genera una lista de pizzas
pizzas = ['tocino y aceitunas','anchoas','peperoni','mexicana','vegetariana',
          'italiana','cajeta y nuez']
# Imprime un comentario usando cada sabor de pizza en las listas
for pizza in pizzas:
    print(f'la pizza de {pizza.title()} es buena')
print('Realmente me gusta la pizza')

# Imprime una lista de numeros del uno al 20 usando for
print([valor for valor in range(1,21)])
# Imprime una lista de numeros del 1 al un millon
numero = [valor for valor in range(1,1_000_001)]
print(numero)
#imprime la suma de todos los numeros generados en cada iteracion
print(f'{sum(numero)}\n')
# Imprime el maximo y el minimo del rango anterior
print(f'el valor maximo es {max(numero)} y el valor minimo es {min(numero)}')

#              ***LIST COMPREHENSION***
# Imprime los numeros impares del rango
print([valor for valor in range(1,21,2)])
# Imprime todos los cubos del rango
print([valor**3 for valor in range(1,21)])
# Genera una nueva lista a partir de los valores de la lista anterior que tienen una 'A'
# sintaxys>> newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Imprime solo una parte de una lista ya existente
print(f'Las primeras tres pizzas del menu son {pizzas[:3]}')                   
# Imprime solo las pizzas en medio de la lista
print(f'Las pizzas a medio menu son {pizzas[3:6]}')
# Imprime solo las pizzas al final del la lista
print(f'Las pizzas al final del menu son {pizzas[5:]}')
# Crea una nueva lista a partir de la lista anterior y agrega elementos a cada lista
pizzas_de_mi_amigo = pizzas[3:6]
pizzas.append('tres quesos')
pizzas_de_mi_amigo.append('hawaiana')
print(f'Mi menu es {pizzas}')
print(f'El menu de mi amigo es{pizzas_de_mi_amigo}')

# usando or y and en una comprobacion if
edad = 22 
edad_2 = 18
comprobacion = edad_2 >= 21 or edad >= 21
print(comprobacion)

# Comprobando existencia de valores en una lista
ingredientes = ['peperoni','salda de tomate','anchoas','pina','chorizo',
                'queso','tocino','pimientos','champinones']

ingrediente = 'peperoni' in ingredientes
print(f'el ingrediente {ingrediente} esta incluido')
ingrediente = 'salchicha' in ingredientes
print(f'el ingrediente {ingrediente} no esta incluido')