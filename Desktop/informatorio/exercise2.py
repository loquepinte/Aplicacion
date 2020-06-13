print("Por favor ingrese el numero de acuardo al tamaño del pes:")
tamanio=int(input("1: Normal. 2:Debajo de lo normal. 3:Un poco encima de la normal. 4:Muy encima de lo normal: "))
while tamanio<1 or tamanio> 4:
    print("Ingreso mal el valor")
    print("Por favor ingrese el numero de acuardo al tamaño del pes")
    tamanio=int(input("1: Normal. 2:Debajo de lo normal. 3:Un poco encima de la normal. 4:Muy encima de lo normal"))    
if tamanio==4:
     print("Pez contaminado")
elif tamanio==3:
    print("Pez con síntomas de organismo contaminado")
elif tamanio==2:
    print("Pez con problemas de nutrición")
elif tamanio==1:
    print("Pez en buenas condiciones")
