saldo = []

menu = True
while menu:
    print("="*20, "\n")
    print("Bienvendio a tu cajero")
    print("="*20, "\n")
    
    print("1. Depositar dinero")
    print("2. Ver saldo en la cuenta")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir de la cuenta")
    
    escoger=int(input("¿Cuál es tu opción? (1-5): "))
    if escoger == 1:
            valor=int(input("Ingresa el valor que vas a depositar: "))
            saldo.append(valor)
            print(saldo)
            continue
        
    if escoger == 2:
        print(f"Tu saldo es:", saldo)
        continue
    
    if escoger == 3:
        retirar=int(input("¿Cuánto dinero deseas retirar?: "))
        if retirar > saldo:
            print("Saldo insuficiente") 
            

        
        
            
        
        
        
    
        
        
            
        
            
    

            