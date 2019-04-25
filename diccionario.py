"""
diccionario{}

nombre_de_diccionario={"nombre clave":"valor"}
#lista
persona = ["marce", 32, "programador"]
#diccionario


dic_persona = {"nombre":"Marce", "Edad":32}
dic_persona["Edad"]
"""


#crear un diccionario persona con las claves nombre, edad, estatura e imprimi cada uno de los valores de las claves
# un print diferente

#luego cambiar la edad a otrp valor e imprimir de nuevo
#lueeego agregar un par de clave hobbie que contenga una ******lista*****
#de hobbies e imprimir todo el diccionario
dicchoto={"nombre":"Matias", "edad":22,"altura":180}
dicchoto.get("nombre")
dicchoto.get("edad")
dicchoto.get("altura")

vari = input("nueva edad")
dicchoto["edad"]= vari
print(dicchoto.get("edad"))

pasatiempos = ["escuchar musica","jugar","salir"]
dicchoto["hobbie"]= pasatiempos
print(dicchoto)
