nota1=int(input("Ingrese el 1° Nota: "))
porcentajeNota1=(nota1*10)/100
nota2=int(input("Ingrese la 2° Nota: "))
porcentajeNota2=(nota2*10)/100
nota3=int(input("Ingrese la 3° Nota: "))
porcentajeNota3=(nota3*15)/100
nota4=int(input("Ingrese la 4° Nota: "))
porcentajeNota4=(nota4*20)/100
nota5=int(input("Ingrese la 5° Nota: "))
porcentajeNota5=(nota5*45)/100
print("el 10% de la nota1 es : ",porcentajeNota1)
print("el 10% de la nota2 es : ",porcentajeNota2)
print("el 15% de la nota3 es : ",porcentajeNota3)
print("el 20% de la nota4 es : ",porcentajeNota4)
print("el 45% de la nota es : ",porcentajeNota5)

resultadoTotal=porcentajeNota1+porcentajeNota2+porcentajeNota3+porcentajeNota4+porcentajeNota5
print("la nota final es : ",resultadoTotal)