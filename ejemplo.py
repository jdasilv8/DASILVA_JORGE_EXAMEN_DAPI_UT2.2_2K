corredor = {}

while True:     
    progreso = input("Indique la hora y el kilómetro con el formato (XX:XX KmXX): ")
    hora , km = progreso.split()
    corredor[hora] = km

    final = input("Ha acabado la carrera? si/no: ")
    if final == 'si':
        claves = list(corredor.keys())
        values = list(corredor.values())
        for i in range (len(corredor)):
            print ('El corredor a las', claves[i],'estaba en el', values[i])
        break