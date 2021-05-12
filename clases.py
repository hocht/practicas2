class restaurante:
    # Un simple intento de modelar un restaurante

    def __init__(self,nombre,tipoDeCocina):
        # inicializando los atributos nombre y tipo de cocina
        self.nombre = nombre
        self.tipoDeCocina = tipoDeCocina
        self.comensales = 0

    def describirRestaurante(self):
        # metodo que describe que tipo de restaurante es
        print(f"el restaurante {self.nombre} es del tipo {self.tipoDeCocina}. \n")
    def abrirRestaurante(self):
        # metodo que simula la apertura del restaurante
        print(f"El restaurante {self.nombre} esta abierto.\n")
    def numeroDeComensales(self):
        # metodo que muestra el numero de comensales atendidos en el dia
        print(f"hemos atendido a {self.comensales} comensales.\n")
    def incrementarComensales(self,personas):
        # incrementa el numero de comensales
        if personas >= self.comensales:
            self.comensales += personas
        else:
            print("no puedes restar personas al numero de comensales") 
        
miRestaurante = restaurante('la joya','cocina italiana')
print(f"el nombre de mi restaurante es {miRestaurante.nombre.title()}.\n")
print(f"{miRestaurante.nombre.title()} es un restaurante de {miRestaurante.tipoDeCocina}.\n")
miRestaurante.describirRestaurante()
miRestaurante.abrirRestaurante()
miRestaurante.numeroDeComensales()
miRestaurante.incrementarComensales(56)
miRestaurante.numeroDeComensales()


