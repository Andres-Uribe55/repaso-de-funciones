def saludar():
    nombre = input("Ingresa un nombre: ")
    print(f"Hola {nombre} espero que tengas un buen día")
    
def suma():
    numero1 = int(input("Ingresa un número: "))
    numero2 = int(input("Ingresa un número"))
    suma = numero1 + numero2
    print(suma)
    
def par_impar():
    num = int(input("Ingresa un número: "))
    if num % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
        
def mayor_edad():
    edad = int(input("Ingresa su edad: "))
    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
        
def fahrenheit():
    temperatura = int(input("Ingrese la temperatura en Celsius: "))
    conversor = (temperatura * 9/5) + 32
    print(f"la temperatura {temperatura} en Fahrenheit es {conversor}")
    
def area():
    base=int(input("Ingresa la base del triangulo: "))
    altura=int(input("Ingresa la altura del triangulo"))
    area=(base*altura)/2
    print(f"La area del triangulo es {area}")


  
def lista():
    numeros=input("Ingresa una lista de números separadas por ',': ")
    lista=numeros.split(",")
    lista=[int(i) for i in lista]
    mayor=max(lista)
    print(f"El número mayor es {mayor}")
    
def palabra():
    palabra = "esternocleidomastoideo"
    print(palabra)
    letra=input("Ingresa la letra que vas a contar: ")
    repetido= palabra.count(letra)
    #print(palabra.count(letra))
    print(f"la letra se repite {repetido}")
    
def pares():
    list1=[7,9,12,18,23,25,30,]
    for i in list1:
        if i % 2 == 0:
            print(i)
       
    