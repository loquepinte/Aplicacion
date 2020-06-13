nota = float(input("Ingresar una nota: "))
while nota<0 or nota>10:
    print("Ingreso mal el valor")
    nota=float(input("Ingrese de nuevo: "))
if nota >= 9 and nota<10:
    print("Sobresaliente")
elif nota >= 7 and nota<=8:
    print("Notable")
elif nota >= 6 and nota< 7:
    print("Bien")
elif nota <= 5:
    print("Suficiente")
else:
    print("Insuficiente")  



    
    