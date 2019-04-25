import requests
from pprint import pprint
API_KEY ="595695c3"
URL= "http://www.omdbapi.com/?apikey="
titulo="The Matrix"

busqueda = URL + API_KEY+ "&t=" + titulo

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()
#pprint(dic_peli)
print(dic_peli["Year"])

#ej1. consultar el api de OMDB e pri,ir el nombre de director de the fight club
#ej2. crear una funcion que reciba como argumento el titulo de una pelicula y retorne lo actores de essa pelicula
def Actores(nombre_peli):
    import requests
    from pprint import pprint
    API_KEY ="595695c3"
    URL= "http://www.omdbapi.com/?apikey="
    titulo= nombre_peli

    busqueda = URL + API_KEY+ "&t=" + titulo

    respuesta = requests.get(busqueda)
    dic_peli = respuesta.json()
    pprint(dic_peli)
    print(dic_peli["Actors"])
Actores("The Revenant")

