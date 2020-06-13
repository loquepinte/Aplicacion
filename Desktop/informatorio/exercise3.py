print("Tiene el compuesto X en el suelo:")
existe=int(input("1:Si lo tengo puesto.  2:No lo tengo puesto "))
if existe==1:
    valor=float(input("Ingrese el porcentaje por hectarea, sin poner el por ciento al final : " )) 
    if valor>10:
        valor=int(input("Uste tiene vegetación tipo matorral en su campo 1:SI 2:NO "))
        if valor== 1:
            print("Su campo esta en condiciones de usar fertilizante")
        else:
            print("Su campo no esta es apto para la utilizacion de fertizante")        
    else:
        print("Su campo no esta es apto para la utilizacion de fertizante")        
else: 
    print("Su suelo no es apto para la utilización de fertilizante")
