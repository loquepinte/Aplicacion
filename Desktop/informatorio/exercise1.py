valor= float(input("¿Cuantos años viene usando insecticida?, Ingrese el nro de años: "))
while valor<0:
     print("ingrese de nuevo el valor")
     valor= float(input("¿Cuantos años viene usando insecticida?, Ingrese el nro de años: "))
if   valor>10:
     print("Por favor solicite revisión de suelos en su plantación")
else: 
     print("Intentaremos ayudarte con un nuevo sistema de control de plagas, y cuidaremos el suelo de tu plantación")     
            