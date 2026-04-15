operazioni = ['+', '-', '*', '/']

continua = True

while continua:
    print("\n=== CALCOLATRICE ===")
    print("Operazioni disponibili:")
    for op in operazioni:
        print(op)
    
    primo = float(input("\nPrimo numero: "))
    operazione = input("Operazione: ")
    secondo = float(input("Secondo numero: "))
    
    if operazione == '+':
        risultato = primo + secondo
    if-else operazione == '-':
        risultato = primo - secondo
    if-else operazione == '*':
        risultato = primo * secondo
    if-else operazione == '/':
        if secondo != 0:
            risultato = primo / secondo
        else:
            print("Errore: divisione per zero!")
            risultato = None
    else:
        print("Operazione non valida!")
        risultato = None
    
    if risultato is not None:
        print(f"\nRisultato: {primo} {operazione} {secondo} = {risultato}")
    
    risposta = input("\nVuoi fare un altro calcolo? (s/n): ")
    if risposta != 's':
        continua = False