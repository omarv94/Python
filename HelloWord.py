# print ("hello word")
# numero1 =int(input('Ingrese numero 1 : '))
# numero2 =int(input('Ingrese numero 2 : '))
# numero3 =int(input('Ingrese numero 3 : '))

# if numero1 == numero2 and numero1 == numero3:
#     print('Empate')
# elif numero1 == numero2 and numero1 > numero3:
#     print('numero uno y numero dos son mayores') 
# elif numero2 ==numero3 and numero2 > numero1:
#     print('numero dos y numero 3 son mayores ') 
# elif numero1 == numero3 and           


#for structure
suma=0
for i in range(5):
    suma = suma + int(input('ingrese un nuevo numero : '))

print(suma)

#while structure


suma = 0
while True:
    suma = suma + int(input('ingrse numero : '))
    stop = input('Desea cuntinuar S/si N/no')
    if stop != "S" and stop != "s":
        break

print(suma)    


suma =0
num1 =0
num2 =0
while True:
    while True:
         num1 = int(input('ingrese un numero de el 1-5'))
         if num1 > 1 and num1 < 5:
             break
         else:   
            print('numero Erroneo debe ser un numero de 1 a 5')

    while True:
     num2 = int(input('ingrese un numero de el 5-9'))
     if num2 > 6 and num2 <10:
         break
     else:
         print('numero incorrecto, Debe ser un numero entre 6 y 10')   

suma = suma +num1 +num2
stop = input('Desea cuntinuar S/si N/no')