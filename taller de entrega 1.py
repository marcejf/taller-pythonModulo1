# letras del afabeto 
def  ejercicio1():
 letra = (input("escriba una letra aqui,  por favor: "))

 if letra >= "a" and letra <= "m":
    print(" le letra que escribio pertenece a las primeras letras del alfabeto")
 else:
    print("la letra que escribio pertenece a las ultimas letras del alfabeto ")
        


     
# angulos 
def ejercicio2(): 
 angulo = int(input("ingresa el angulo "))
      
 if 0 <= angulo < 90:
        print("el angulo digitó se encuentra en el cuadrante 1 : ")
 elif 90 <= angulo < 180:
        print("el angulo que digitó  se encuentra en el cuadrante 2 : ")  # revisar
 elif 180 <= angulo < 270:
        print(" el angulo que digito  se encuentra en el cuadrante 3 :")
 elif 270 <= angulo < 360:
        print("el angulo que digito se encuentra en el cuadrante 4 :")
 else:
   print("el angulo que digito no es valido :(")
     
# notas 

def ejercicio3():
 n = float(input("escriba aqui su nota : "))

 try:
    #n=float(n)
    if n > 4.5:
        print("excelente ")
    elif 3.5 <= n <= 4.4:
        print("bueno ")                     
    elif 3 <= n <= 3.4:
        print("regular")
    elif 0 <= n <= 2.9:
        print("malo ")
    else:
        print("no es una nota valida ")
 except ValueError:
    print("POR FAVOR INGRESA UN VALOR NUMERICO ")        

 
 # temperatura 
def ejercicio4():
 temperatura = float(input("ingresa la temperarura "))
 if temperatura >= 0 and temperatura <= 10:
    print("frio")
 elif temperatura >= 11 and temperatura <= 34:
    print("templado")
 elif temperatura  >= 35 and temperatura <= 40:
    print("calido")
 else:
    print("temperatura no ideal")

# verificar la palabra Jengibre
def ejercicio5():
 palabra = str(input(" escriba la palabra Jengibre: ")) 

 if palabra == "Jengibre":
    print("si, el Jengibre es la major planta de todos los tiempos")
 elif palabra == "jengibre":
    print("No, quiero un gran gengibre")
 else:
    print("¡Jengibre!, NO")


# contar numeros inversos 
def ejercicio6():
 continicial = 20
 final = 1
 while continicial >= final: 
    print(continicial)  
    continicial -= 1  


# numeros hasta el 50 de 2 en 2
def ejercicio7 (): 
 numero1 = 1 
 numero2 = 50
 while numero1 <= numero2:
    print(numero1)
    numero1 += 2
 

def ejercicio8():
 texto = input("escriba aqui : ")
 vocales = "aeiouAEIOU"
 contador = 0 

 indice = 0
 while  indice < len(texto):                 
    if texto[indice] in vocales:
        contador += 1
    indice += 1
    
 print(" el texto que escribio tiene",len(texto), "vocales")

# numero de dados

def ejercicio9():

 acerto_dado = 6
 while acerto_dado:
        intento = int(input("intentalo hasta acertar (): "))                                      
        if intento > acerto_dado:
            print("ingresa un numero mas bajo")
        elif intento < acerto_dado:
            print("ingrese un numero mas alto : ")
        else:
            print("acertaste ") 
            break
        
        
        
# suma de numero
def ejercicio10():
    suma = 0
    while True:
        numero1 = input("escribe el numero ( y escribe 0 para terminar): ")
        if  numero1 == "0":
            break
        if numero1.isdigit():
            suma += int(numero1)
        else:
            print("por favor, ingresa un numero valido :) ")
    print("la suma es :", suma)        


#suma de cubos hasta el 50
def ejercicio11():
 sumarCubos = 0
 for i in range(1,50):
    cubos = i **3
    sumarCubos += cubos
 print("la suma de los cubos es : ", sumarCubos)    
    
#triangulo 


def ejercicio12():
 filas = (5)
 for i in range(filas):
     print(" " * (filas - i - 1), end="")
     print("*" * (2 * i +1 ))      
     
     
    # ajedrez 
def ejercicio13():      
 n = 8
 for i in range(n):
    for j in range(n):
        if(i+j) % 2 == 0:
            print("#", end= " ")
        else:
            print("0", end=" ")
    print()        


#invetir cadena 
def ejercicio14():
    cadena = input("ingresa una cadena : ")
    invertirCadena = ""

    for char in cadena:
     invertirCadena = char + invertirCadena
    print("cadena invertida: ", invertirCadena)    



def ejercicio15():
    lista_decaracteres = print(['casa','cama','patio','jardin','carro','piscina'] )             #revisar
    buscar_elemento = input("¿que elemento deseas buscar ? : ")   
    elemento_encontrado = False 

    for i in range(len(lista_decaracteres)):
        if lista_decaracteres[i] == buscar_elemento:
            print(f"el elemento que buscas esta en la posicion {i+1}")
            elemento_encontrado = True
            break
        if not elemento_encontrado:
            print("el elemento no se encuentra en la lista ")    
        
    
#lambda suma
    
def ejercicio16():
    sumar = lambda x, y: x + y 
    print(sumar(4,7)) 

# par o impar
def ejercicio17():
    numeroPar =lambda x: x % 2 == 0
    numero = int(input("digita un numero : "))                        
    if numeroPar(numero):
        print("el numero es par")  
    else:
        print("el numero es impar ")       

 
 
#ordenar tuplas 
def ejercicio18():
 tuplas = [(1,2),(7,8),(3,4),(5,6)]

 tuplas_ordenadas = sorted(tuplas,key=lambda x : x[1])
 print(tuplas_ordenadas)
             
#tuplas numeros mayores a 10
def ejercicio19():
 numeros = [5,67,34,2,0,8,10,56,32,19,15]  
 nummayoresa_10 = list(filter(lambda x : x > 10, numeros)) 
 print(nummayoresa_10)          


#funcion lambda para elever numeros al cuadrado 
def ejercicio20():
 numerosaelevar = [1,2,3,4,5,6,7,8,9]
 cuadrados = list(map(lambda x: x**2,numerosaelevar))
 print(cuadrados)

def main():
    while True:
        print("\nMENU DE EJERCICIOS DE PYTHON")
        print("1.  ejercicio 1")
        print("2.  ejercicio 2")
        print("3.  ejercicio 3")
        print("4.  ejercicio 4")
        print("5.  ejercicio 5")
        print("6.  ejercicio 6")
        print("7.  ejercicio 7")
        print("8.  ejercicio 8")
        print("9.  ejercicio 9")
        print("10. ejercicio 10")
        print("11. ejercicio 11 ")
        print("12.  ejercicio 12")
        print("13.  ejercicio 13 ")
        print("14. ejercicio 14 ")
        print("15 ejercicio 15 ")
        print("16 ejercicio 16")
        print("17.  ejercicio 17")
        print("18.  ejercicio 18")
        print("19  ejercicio 19")
        print("20  ejercicio 20")
        print("21  SALIR")
        
        opcion = input("ingresa la opcion: ")
        
        if opcion == "1":
            ejercicio1()
        elif opcion =="2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif  opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion ==  "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9() 
        elif opcion == "10":
            ejercicio10()
        elif opcion == "11":
            ejercicio11()
        elif opcion == "12":
            ejercicio12()
        elif opcion == "13":
            ejercicio13()
        elif opcion == "14":
            ejercicio14()
        elif opcion == "15":
            ejercicio15()
        elif opcion =="16":
            ejercicio16()
        elif opcion == "17":
            ejercicio17()
        elif opcion == "18":
            ejercicio18()
        elif opcion == "19":
            ejercicio19()
        elif opcion == "20":
            ejercicio20()
        elif opcion == "21": 
            print("adios") 
            break 
        else:
            print("opcion invalida, intenta de nuevo")
        
if __name__=="__main__":   
 main()

