
Saltar al contenido
Tablero
Hyrum Lopez Orozco
Cuenta
Tablero
Cursos
Calendario
Bandeja de entrada
Historial
Kaltura
My Media
Ayuda
CS 1400 WSD Fall 2026 23008
Tareas
📝 M7 Tarea Diccionarios

Fall 2026
Página de Inicio
Anuncios
Programa del curso
Módulos
Student Resources
Calificaciones1
Starfish
Cuaderno
📝 M7 Tarea Diccionarios
Fecha de entrega: sáb 17 de oct de 2026 23:59
30 Points Possible

En progreso
SIGUIENTE: Presentar tarea

Unlimited Attempts Allowed
Diccionarios
Agregar, reemplazar y eliminar elementos de un diccionario

Observa el segmento de código a continuación y luego responde las preguntas.

Observa el diccionario num_salon en el código de abajo. ¿Qué signo de puntuación separa la clave (key) del valor (value)?

Nota la coma al final de cada par clave-valor. ¿Por qué crees que no hay una coma después de "Cruz"?
¿Cuántos pares clave-valor hay inicialmente en el diccionario?

Ejecuta el programa. ¿Qué reporta la función len() como la longitud del diccionario?

Agrega a "DeLeon" al diccionario asignándole el salón 147.

Ejecuta el programa. ¿Cambia la longitud del diccionario al agregar a DeLeon?

Observa la puntuación para agregar elementos adicionales al diccionario. Agrega un instructor adicional "Hernandez" con el número de salón 323. Asegúrate de usar los corchetes [] para agregar al instructor.

Ejecuta el programa. ¿Qué se imprime cuando se usa el método .get() al imprimir el instructor Valle? ¿La clave o el valor?

¿Qué se imprime cuando usas los corchetes para imprimir los datos?

¿Ves alguna diferencia entre acceder a los datos usando los corchetes [] y el método .get()?

Agrega una sentencia print para imprimir el número de salon de Murphy.

num_salon = {
    "Murphy": 304,
    "Feiz": 336,
    "Mack": 207,
    "Ball": 227,
    "Bristow": 321,
    "Cruz": 101
}

print("La longitud es", len(num_salon))

# Agregar un elemento adicional al diccionario
num_salon["Valle"] = 216
print("La longitud ahora es ", len(num_salon))

print( num_salon.get("Valle") )
print( num_salon["Murphy"])
Copia Superficial vs. Copia Profunda
(Shallow VS Deep Copy)
Los siguientes pares clave-valor representan la cantidad de animales en un refugio. Practica observando y programando lo siguiente.

¿Cuántos perros hay en el refugio al principio?

¿Cuántos perros se están agregando al refugio?

Escribe la línea de código para eliminar 3 gatos del refugio.

Observa el código para agregar los hurones. ¿Cuántos se agregaron?

Escribe el código para agregar 4 serpientes al refugio.

Escribe una sentencia if para imprimir "Lleno" si el número de perros es mayor a 50.

Escribe una sentencia if para imprimir "No Ratones" si "raton" no es una clave en el diccionario animalesRefugiados.

Nota que la variable refugioOriginal es igual a la variable animalesRefugiados. ¿Es esta una copia superficial o profunda?

Escribe el comando para mostrar los animales de refugioOriginal al final del segmento de código. ¿Muestra los animales originales?

Cambia refugioOriginal para que sea una copia profunda (deep copy) de animalesRefugiados (recuerda importar la librería copy). ¿Muestra los animales originales ahora?

¿Qué diferencia notas entre una copia profunda y una copia superficial?

Python
import copy

animalesRefugiados = {"perro": 49, "gato": 38, "conejo": 14}
refugioOriginal = animalesRefugiados
animalesRefugiados['perro'] += 2
animalesRefugiados["huron"] = 2
print(animalesRefugiados)
Uso de Diccionarios
El siguiente segmento de código contará cuántas veces aparece cada palabra en el texto dado.

Observa la variable listaNotas. ¿Es una lista o un diccionario?

¿Qué hace la función split()? (Puedes consultar lecciones anteriores).

Observa la variable notasDiccionario. ¿Está definida como una lista o un diccionario?

¿Hay valores en el diccionario o está vacío?

Observa el bucle for. ¿Está iterando a través de la lista o del diccionario?

Dado que la primera puntuación en listaNotas es "A", ¿el código ejecutaría la sentencia if o la sentencia else dentro del bucle?

El comando es notasDiccionario[i] = 1, cuando i es igual al texto "A", ¿cuál es el par clave-valor que se agrega al diccionario?

La calificación "A" se agrega varias veces. La primera vez, pasa por el if. La segunda vez, pasará por el comando else. Hablando de esa segunda vez cuando i = "A", el par clave-valor es inicialmente "A": 1, ¿a qué valor se actualiza cuando se ejecuta el comando notasDiccionario[i] += 1?

Ejecuta el programa, ¿cuántas veces aparece la calificación "A" en los puntajes?

Python
# Ejemplo de conteo de palabras
text = "sana sana curita de rana sana sana pomada de sapo sana sana hoy y manana manana y hoy"

lst = text.split()
plbList = dict()

for x in lst:
    if x not in plbList:
        plbList[x] = 1
    else:
        plbList[x] += 1

for i in plbList:
    print (i, plbList[i])

# Ejemplo de conteo de calificaciones
notas = "A A A B B A C A B C C E A B A C C C A B B B A B A A A C D A B B C C A A A B A B A C A B B A"
listaNotas = notas.split()
notasDiccionario = dict()

for i in listaNotas:
  if i not in notasDiccionario:
    notasDiccionario[i] = 1
  else:
    notasDiccionario[i] += 1

for i in notasDiccionario:
  print(i, notasDiccionario[i])
Elegir un tipo de presentación





