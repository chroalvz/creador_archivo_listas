import random
import datetime

nombres_base = [
    "Carlos", "Ana", "Luis", "María", "Javier", "Sofía", "Diego", "Lucía", "Gonzalo", "Elena",
    "Mateo", "Camila", "Joaquín", "Valeria", "Nicolás", "Martina", "Santiago", "Paula", "Agustín", "Isabella",
    "Tomas", "Victoria", "Lucas", "Daniela", "Gabriel", "Sara", "Ezequiel", "Natalia", "Ignacio", "Abril"
]

apellidos_base = [
    "González", "Rodríguez", "Gómez", "Fernández", "López", "Díaz", "Martínez", "Pérez", "García", "Sánchez",
    "Romero", "Sosa", "Torres", "Álvarez", "Ruiz", "Ramírez", "Flores", "Benítez", "Acosta", "Medina",
    "Herrera", "Aguirre", "Castro", "Molina", "Guzmán", "Giménez", "Rojas", "Vidal", "Peralta", "Silva"
]

calles = ["Av. San Martín", "Belgrano", "Rivadavia", "Mitre", "Sarmiento", "Urquiza", "Av. de Mayo", "Pueyrredón", "Lavalle", "Alvear"]
localidades = ["Palermo", "Rosario de la Cruz", "9 de Julio", "Capitan Mendoza", "La Palta", "San Miguel", "Gral. Pico","25 de Mayo", "Inmaculada Concepcion", "San Martin"]
provincias = ["Buenos Aires", "Santa Fe", "Córdoba", "Mendoza", "Tucumán", "Salta", "Neuquén", "Entre Ríos", "Chaco", "Misiones"]

#listado_direccion = []
def fecha():
    fecha_ = datetime.datetime.now().strftime('%d%m%Y_%H%M')
    return fecha_

def datos_persona():
    nombre = random.choice(nombres_base)
    nombre_mail = nombre
    apellido = random.choice(apellidos_base)
    apellido_mail = apellido
    calle = random.choice(calles)
    numero = random.choice(range(0,10000))
    localidad = random.choice(localidades)
    provincia = random.choice(provincias)
    correo = f'{nombre_mail}{apellido_mail}@correo.com'
    edad = random.choice(range(18,85))
    documento = random.choice(range(11000000, 48000000))
    lista = (nombre,apellido,calle,numero,localidad,provincia,correo.lower(),edad,documento)
    return lista

def quitar_acentos_simple(texto):
    con_acento = "áéíóúÁÉÍÓÚñÑ"
    sin_acento = "aeiouAEIOUñÑ"
    tabla = str.maketrans(con_acento, sin_acento)
    return texto.translate(tabla)

def creacion_direcciones(n=1000):
    for i in range(n):
        persona = datos_persona()
        listado = f'{persona[0]};{persona[1]};{persona[2]} {persona[3]};{persona[4]};{persona[5]};{quitar_acentos_simple(persona[6])};{persona[7]};{persona[8]}'
        with open(f'lista_usuario_{fecha()}.csv', 'a+') as file:
            file.write(listado)
            file.write('\n')
            file.seek(0)

#creacion_direcciones()
#print(datos_persona())
valor = input('ingrese la cantidad de lineas que quiere tener para armar el archivo: ')
n = int(valor)
creacion_direcciones(n)
print('fin del archivo')
