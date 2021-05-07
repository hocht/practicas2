#alimentar una lista de otra por medio de un ciclo for
listaDePedidos = ['sandwich de jamon','sandwich de atun',
                  'sandwich montecristo','sandwich de jamon',
                  'sandwich de aceitunas y jamon serrano','sandwich imperial',
                  'sandwich de tres quesos','sandwich de salmon',
                  'sandwich italiano','sandwich de salmon','sandwich italiano',
                  'sandwich de pavo y verduras','sandwich de ensalada de atun',
                  'sandwich de mermelada y crema de cacahuate',
                  'sandwich de frijoles','sandwich poblano',
                  'sandwich de aceitunas y jamon serrano','sandwich de asada',
                  'sandwich de pavo y verduras','sandwich de salmon',
                  'sandwich de asada','sandwich de tres quesos',
                  'sandwich de jamon','sandwich montecristo',
                  'sandwich de atun','sandwich de atun','sandwich imperial',
                  'sandwich de pavo y verduras','sandwich poblano',
                  'sandwich de aceitunas y jamon serrano','sandwich imperial',
                  'sandwich de atun','sandwich de pavo y verduras',
                  'sandwich de pastrami','sandwich mediterraneo',
                  'sandwich de pastrami','sandwich mediterraneo',
                  'sandwich imperial','sandwich de asada',
                  'sandwich de tres quesos','sandwich de salmon',
                  'sandwich de jamon','sandwich de tres quesos',
                  'sandwich de atun','sandwich de pavo y verduras',
                  'sandwich de tres quesos','sandwich de pastrami','sandwich imperial',
                  'sandwich de frijoles','sandwich poblano','sandwich de jamon',
                  'sandwich poblano','sandwich de atun','sandwich de tres quesos',
                  'sandwich de jamon','sandwich de atun','sandwich de tres quesos']
sandwichesListos = []

while listaDePedidos:
    sandwich = listaDePedidos.pop()
    if sandwichesListos.count(sandwich) == 5:
        print(f'Lo sentimos el {sandwich} se ha terminado :( '
        '\nPuedes elegir uno diferente en el menu \n')
        if listaDePedidos.count(sandwich) > 0:
            listaDePedidos.remove(sandwich)
    else:
        print(f'Tu {sandwich.title()} se esta preparando \n' 
        'Gracias por tu paciencia :) \n')
        sandwichesListos.append(sandwich)
    
for sandwich in set(sandwichesListos):
    print(f"el {sandwich} se preparo {sandwichesListos.count(sandwich)} veces")
        
            