# Abrimos el archivo
archivo = open("datos/dataset_partidos.csv", "r")
# Leemos todas las lineas
lineas = archivo.readlines()
# Cerramos archivo
archivo.close()
# Mostramos lineas para verificar
print(lineas)
# Diccionario de victorias
victorias = {}
# Variables
total_goles = 0
cantidad_partidos = 0
# Recorremos lineas
for linea in lineas:
    # Saltamos encabezado
    if "Equipo_Local" in linea:
        continue
    # Eliminamos espacios y saltos
    linea = linea.strip()
    # Si la linea esta vacia la ignoramos
    if linea == "":
        continue
    # Separamos datos
    datos = linea.split(",")
    # Guardamos informacion
    local = datos[0]
    visitante = datos[1]
    goles_local = int(datos[2])
    goles_visitante = int(datos[3])
    # Contamos goles
    total_goles += goles_local + goles_visitante
    # Contamos partidos
    cantidad_partidos += 1
    # Verificamos ganador
    if goles_local > goles_visitante:
        if local not in victorias:
            victorias[local] = 0
        victorias[local] += 1
    elif goles_visitante > goles_local:
        if visitante not in victorias:
            victorias[visitante] = 0
        victorias[visitante] += 1
# Calculamos promedio
promedio = total_goles / cantidad_partidos
# Mostramos resultados
print("TABLA DE POSICIONES")
for equipo in victorias:
    print(equipo, ":", victorias[equipo])
print("PROMEDIO DE GOLES")
print(promedio)
# Guardamos resultados
resultado = open("resultados/resultados.txt", "w")
resultado.write("TABLA DE POSICIONES")
for equipo in victorias:
    resultado.write(equipo + " : " + str(victorias[equipo]) + "")
resultado.write("PROMEDIO DE GOLES\n")
resultado.write(str(promedio))
resultado.close()
print("Resultados guardados correctamente")