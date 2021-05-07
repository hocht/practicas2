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
                  'sandwich de pastrami','sandwich mediterraneo'
                  'sandwich de pastrami','sandwich mediterraneo'
                  'sandwich imperial','sandwich de asada']
sandwichesListos = []

while listaDePedidos:
    sandwich = listaDePedidos.pop()
    print(f'Tu {sandwich.title()} se esta preparando \n' 
           'Gracias por tu paciencia :)')
    sandwichesListos.append(sandwich)

print(f'estos fueron los sandwiches preparados{sandwichesListos}')
