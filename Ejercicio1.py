def LeerDocumento():
    """Función que lee el fichero y lo guardará en una variable como lista

    Parámetros: -Ruta de acceso al fichero
    Salida: Lista con el contenido del fichero"""

    file = open ('LibroCuentas.txt', 'r')
    lineas = file.readlines()
    file.close()
    return lineas

def IdentificarPagado(lista):
    """ Función que lee la lista creada anteriormente y crea un fichero con los artículos ya pagados

    Parámetros: Lista con lo articulos pagados
    Salida: Nada"""
    with open ('Pagado.txt','w') as file:
        for i in lista:
            if "PAGADO" in i:
                texto = ( str(i))
            file.write (texto)
    return



IdentificarPagado(LeerDocumento())