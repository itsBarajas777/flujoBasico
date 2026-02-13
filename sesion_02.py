# Tuplas 
mi_tupla = (2, 4)
print("Mi tupla: ",mi_tupla)

# Lista 
mi_lista = [ 1, 3.1416, "Barajas", mi_tupla]
print("El primer elemento de mi lista:", mi_lista[0])
print("El cuarto elemento de mi lista: ", mi_lista[3])
print("El tercer elemento de mi lista: ",mi_lista[2])

# Diccionarios
mi_diccionario = {"mi_lista": mi_lista,
                  "Nombre": "Barajas",
                  "pi": 3.1416,
                  "Tel": "664-747 7042"}
print("Llave para accesar a mi diccionario mi_lista", mi_diccionario["mi_lista"])
print("Llave para accesar a mi diccionario pi", mi_diccionario["pi"])
print("Llave para accesar ami diccionario Tel",mi_diccionario["Tel"])
