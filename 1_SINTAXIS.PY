  ## CICLOS Y CONDICIONES
#while---------------------- mientras
#while contador>=1:--------- while se usa para un ciclo que se brincara hasta que se cumpla lo pedido de while
#pass----------------------- es guardar un ticket mientras programas lo demas 
#break---------------------- para romper una funcion y que ya no suceda
#conrinue------------------- para brincar si una funcion se cumple 
#if------------------------- si es cierto actua
#elif----------------------- esta es otra opcion de if
#else----------------------- si ningun if se actuo, se actuara este (no es necesario usarlo)
#for elemento in lis-------- por cada ("elemento") en lis
#for valor in numero:------- creando una variable (valor) para usar en una lista (numero) 
#for valor=valor+numero----- ejemplo de como subir el valor de "valor" con el valor de "numero"
#for letra in "string"------ usar un string en un ciclo for directamente
#for letra in [1,2,3]------- usar una lista en un ciclo for directamente
#for letra in (1,2,3)------- usar una tupla en un ciclo for directamente
#range(10)------------------ colocar un rango, en este caso ira del 0 al 10
#range(3,7)----------------- para dar un rango, en este caso ira desde el 3 hasta el 7
#range(2,10,3)-------------- es un rango, pero el terver valor significa en los pasos que va a ir brincanco esntre el rango en este caso sera 3
#n for n in "python"-------- ejemplo de simplificar una linea de un ciclo 
#match variable:------------ es una opcion simplificada de uso de for, usando match se usa case
#


  ## LISTAS Y DICCIONARIOS
#insert(i,"x") ------------- aqui decides donde colocar el valor en la lista donde i esla posicion y la "x" es el valor que meteras
#append(x) ----------------- aqui solo agregas sin poder colocarlo donde quieras
#lista = [] ---------------- se usan corchetes []
#diccionario = {} ---------- se usan llaves {}
#range(-1,-11,-1) ---------- range (inicio,final,paso)
#lista.keys ---------------- este es para sacar la llave, no el valor
#lista.values -------------- esta es para usar el valor, no la llave
#.sort() ------------------- para ordenar alfabeticamente o ascendente de numeros pero solo de un tipo
#.reverse()----------------- ordena todo pero de manera inversa o desendente 
#.sorted() ----------------- si devuelve los valores para poder usarse
#.len() -------------------- para saber cuantos elementos/letras tiene la lista
#.count(VALOR) ------------- para saber cuantas veces se repite VALOR
#.copy() ------------------- con esto podemos copiar todo los valores de una lista
#.clear() ------------------ se elimina o limpia todos los valores de una lista
#.get() -------------------- puede usarse para poner valor y puedes definir un mensaje si no existe ese valor
#.split(" ")---------------- el valor de la variable se separará por cada valor dado en este caso es " "
#print(list+list2)---------- se pueden concatenar dos listas o mas 
#list1[0]="culo"------------ cambia el valor de la celda 0 de list1 a "culo"
#list.pop(2)---------------- elimina o brinca el valor de la casilla 2
#print(v(list1.pop(2))------ uso de el valor eliminado o brincado, ojo se tiene que usar su variable donde se almaceno el .pop(2)
#lista.append("g")---------- se agrega "g" en la lista
#c=(s["carro"])------------- una variable con el valor de "apellido" en la lista s
#dic["c1"][0]--------------- uso de valor en la casilla 1 en el significado de "c1" del diccionario (dic)
#dic[12]="c"---------------- agregar un valor que no existe en un diccionario
#dic[2]="B"----------------- cambiar el sinificado de un valor del diccionario 
#dic.keys()----------------- muestra solo los nombres de los diccionarios
#dic.values()--------------- muestra solo los significados del diccionario 
#dic.items()---------------- muestra todo lo que contiene todo el diccionario
#tupl=list(tupl)------------ convertir tupl a lista
#lis=tuple(lis)------------- convertir lista a tupla


  ## SETS - estos a diferencias solo usan un valor (ignora los valores que se repiten)
#s=set([2,1,4])------------- este es el uso de los set existen dos formas esta es la 1
#s={2,1,4}------------------ esta es la otra manera de usar los set, de esta forma es necesario usar llaves, pytohn de autoamtico lo detecta como set
#prin(2 in s)--------------- para saber si 2 se encuentra en el set, lista o tupla de manera booleana en True o False
#.union()------------------- se usa para unir sets o listas 
#.add(4)-------------------- es para agregar, en este caso se agrega un 4
#.remove(2)----------------- es para remover o eliminar, si no existiera 2 marcaria un error
#.discard(6)---------------- es para descartar per en este caso si 6 no existe no marcaria error
#.clear()------------------- elimina todo lo que contiene el set


  ## BOOLEANO
#n=bool(5<6)---------------- es usar los booleanos pero con la funcion bool
#n=bool()------------------- este es un ejemlo de poner una comparacion en falso inmediatamente
#n=5 in lista--------------- ejemplo de booleano
#n=5 not in lista----------- ejemplo de booleano en negativo


  ## ELIMINAR
#.pop() -------------------- elimina valor de lista
#.popitem() ---------------- elimina significado de diccionario
#.remove() ----------------- eliminar significado de diccionario
# del[] -------------------- funcion para eliminar valores en una lista


  ## SINTAXIS DE USO
#input() ------------------- para pedir datos a usuario
#print() ------------------- print() para imprimir
#print(f"{variable}" ok) --- f dentro sirve para poder colocar una variable dentro de un print
#try:inputva=int(inpuyva)--- try: es para saber si esta bien el dato que pediste
#except:print("no")exit()--- except: es para poner un mensaje si no se puso lo que se pidio
#joto=jotoototote ---------- uso de variables
#string= "Jose Camacho"----- str (letras)
#entero=12 ----------------- int (num. enteros)
#flotantes=10.5 ------------ float (num. con decimales)
#booleano=False ------------ bool (false or true)
#.capitalize() ------------- convierte la primera letra en mayuscula
#texto=texto.upper()-------- upper() texto a mayusculas
#texto=texto.lower()-------- lower() texto a minusculas
#texto=texto.swapcase()----- swapcase() cambia los mayu a minu y viceversa
#variable[2:-5]------------- [:] para indicar desde donde a donde usaras los digitos
#[::-1]--------------------- este se usa para poner en reversa lo que quieras de la variable
#.find()-------------------- es para encontrar algo en la operacion o variable
#"\n"----------------------- se usa para pasar al siguiente renglon
#"\t"----------------------- para tabular en el texto
#"\\"----------------------- para colocar una barra en el texto 
#"hola {} y {}".format(x,y)- para colocar x y y en la oracion de print con ese orden (colocados en el .format())
#.index()------------------- entre parentesis colocas la letra o frase que quieres que te diga la ubicacion del texto o letra
#.rindex()------------------ este la diferencia del .index(), es que este empieza a contar desde la derecha a la izquierda
#.find()-------------------- este es lo mismo que un find pero cuando no encuentra te sale -1 en index no
#string[3]------------------ te dira el valor que esta en esa posicion
#.split()------------------- para separar las frases a listas separados por espacios
#.split("t")---------------- separa la frase separadas por cada "t"
#.startswith("a")----------- verificar si las cosas empiezan con la "a"
#" ".join([a,b,c])---------- se usa para unir variables con la " "
#list.join(separador)------- tambien se puede usar para convertir una lista a str
#a.replace("e","x")--------- en la variable a se cambiara todas las "e" seran "x"     
#""" """-------------------- cuando colocas las tres comillas en el texto puede pasar de renglon con enter en vez de hacerlo con \n
#len(variable)-------------- te dira el largo(numero de digitos) que contiene en este caso la variable
#print(variable*5)---------- la variable se repetira en este caso 5 veces seguidas
#print("agua" in variable)-- para saber si "agua" esta dentro de la variable
#reversed()----------------- para poner invertido los valores de una lista
#enumerate(variable)-------- para enumerar todo lo que esta en la variable, tomando en cuenta que la variable es una lista
#zip(carro,color,placa)----- zip() se utiliza para colocar la informacion de varias listas en tuplas, el zip sera del largo de la lista mas corta de todas las listas
#.lstrip(.,*)--------------- este se usa para eliminar todos los valores de la izquierda en este caso seran .,*
#lis.isdisjoint(lista)------ isdisjoint se usa para saber si se repiten valores en las listas, en este ejemplo usamos tomamos en cuenta si algo de la lista "lis" hay valores que se repiten en la lista "lista"




  ##RANDOM
#randit(1,30)--------------- te dara un numero aleatorio, en este caso entre el 1 y el 30
#uniform(1,5)--------------- te dara un numero con decimales(float) aleatorio en este caso entre el 1 y el 5
#random()------------------- el random se utiliza sin ningun valor y te dara u valor aleatorio entre el 0 y el 1 en float
#choice(listaColors)-------- eligira un valor aleatorio de la lista 
#shuffle(listNumeros)------- colocara de manera aleatoria los numeros de la lista, tener en cuenta que shuffle no se puede usar con strings y es inmutable 



  ##OPERADORES LOGICOS
#or------------------------- es o 
#and------------------------ es y
#not------------------------ negacion de un operador
#("n"in t)and("d"in t)------ uso de operador matematico con variables
#("s" not in a)------------- para saber si "s" no esta en la variable a
#

  ##MATEMATICAS
# % ------------------------ significa el resto de una division 
# // ----------------------- significa el resultado de una divicion (cociete)
# 3= ----------------------- asignacion
# += ----------------------- sumar y asignar
# -= ----------------------- restar y asignar
# *= ----------------------- multiplicar y asignar
# /= ----------------------- dividir y asignar
# **= ---------------------- elevar y asignar
# == ----------------------- igualdad
# > ------------------------ mayor que
# >= ----------------------- mayor igual que
# < ------------------------ menor que 
# <= ----------------------- menor igual que 
# != ----------------------- distinto que
# x**0.5-------------------- para saber la raiz cuadrade de un numero 
#x**2----------------------- al cuadrado y asi sucesivamente
#min()---------------------- para saber cual es el valor mas bajo dentro de la celda   ambos casos se pueden clasificar por numeros mas grandes y alfabeticamente
#max()---------------------- para saber cual es el valor mas alto en las celdas
#max(nombre.values)--------- uso de valores de un diccionario usando en un diccionario





