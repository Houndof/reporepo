class Dino:
    patas= 4
    nombre= None
    def __init__(self, canti_patas,un_nombre):
        self.patas= canti_patas
        self.nombre= un_nombre
        print("hola soy un dinosaurio","me llamo", self.nombre,"y tengo",self.patas)

        def get_patas(self):
            return self.patas

        def set_patas(self, cantidad):
            self.patas= cantidad
pepito= Dino(4, "pepito")

### en el archivo objetos.py Crear una clase persona con atributo nombre
### despues instanciar un objeto de tipo persona
class Auto:
    velocidad= 150
    marca= None
    def __init__(self, marca_auto, velocidad_auto):
        self.velocidad= velocidad_auto
        self.marca= marca_auto
        print("un auto de marca", self.marca, "paso a", self.velocidad, "por hora")
ambos = Auto("toyota", 150)
##modificar la clase persona, agregarle un atributo edad y
# un metodo cumple_anhos y un metodo get_edad
#inicializa/ crear un objeto de tipo persona u hacerle cumplir anhos