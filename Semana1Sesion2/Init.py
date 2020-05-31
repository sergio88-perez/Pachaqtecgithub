datos_basicos = {
    "nombres":"Sergio Leonardo",
    "apellidos":"Perez Tafur",
    "DNI":"45249658",
    "fecha_nacimiento":"21/07/1988",
    "lugar_nacimiento":"Rimac, Lima, Perú",
    "nacionalidad":"Peruano",
    "estado_civil":"Casado"
}
clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print (clave + ": " + valor)