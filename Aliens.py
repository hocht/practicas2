# Un diccionario que incluye la informacion de una persona
andrea = {'edad':'25','altura':'1.93 mts','sexo':'mujer',
          'ciudad':'queretaro'}
print(andrea['edad'])

# un diccionario que incluye informacion sobre los numeros favoritos de varias personas
numerosfavoritos = {'ana':'23','juanita':'32','elena':'12','felipe':'23',
                    'dario':'14','mariana':'23'}

# diccionario de palabras nuevas
glosario = {'tupla':'un conjunto ordenado e inmutable de elementos del mismo o'
            ' diferente tipo.'}

palabra = glosario['tupla']
print(f'el significado de tupla es:  {palabra}')

# glosario de consolas
consolas = {'switch':'nintendo',
            'xbox one':'microsoft',
            'playstation 5':'sony',
            'master system':'atari',
            'megadrive':'sega',
            'gameboy':'nintendo',
            'xbox':'microsoft',
            'playstation':'sony',
            'super nintendo':'nintendo',
            'coleco vision':'coleco',
            'jaguar':'sega',
            'game cube':'nintendo',
            'playstation 2':'sony',
            'ngage':'nokia',
            'ouya':'ouya inc',
            'nintendo 64':'nintendo',
            'xbox series x': 'microsoft',
            'psp':'sony',
            'psp vita': 'sony',
            'nintendo 3ds':'nintendo',
            'gamegear':'sega'
            }
print('\n Estas son las consolas en existencia:\n')

# imprime cada elemento en el diccionario con su etiqueta
for consola,marca in consolas.items():
    print(f'{consola.title()} hecha por {marca.title()}')
# imprime cada consola en la lista
print('\nEsta es una lista de consolas \n')
for consola in consolas.keys():
    print(consola.title())
# Imprime cada marca en la lista en orden y eliminando las repetidas
print('Estas son las companias en la lista')
for companias in sorted(set(consolas.values())):
    print(companias.title())