# Commento
'''
Commento su più righe e DocString
'''
# Python è un linguaggio interpretato : il codice viene
# eseguito riga per riga, non nella sua interezza (compilatore)

print("dlorW olleH"); # print() stampa a schermo...e fino a qua ci siamo
print(5+3); # Stampa la somma dei due numeri

'''
NB: Python è un linguaggio NON tipizzato, non sono obbligato a dichiarare il tipo della variabile
ma per evitare incomprensioni si possono dichiarare.
nome_variabile : tipo_di_dato = valore

Tipi di dato principali in Python:
    int ->  numeri interi
    float -> numeri decimali
    str -> stringhe (testi/caratteri)
    bool -> True/False

CAST (Conversione di tipo di dato):

    nome_variabile_x = valore;
    nome_variabile_y = tipo_di_dato( nome_variabile_x );
'''

x = "10";
y = int(x);

# input() serve a leggere quello che viene scritto su console
# NB: Legge SOLO stringhe

nome = input("Come ti chiami?\n"); # Legge la stringa in input
eta = int(input("Quanti anni hai?\n")); # Legge la stringa in input e la converte in int
# f-string (format string): si scrive una f davanti a tutto e si mettono
# le variabili all'interno delle graffe o concatenando le stringhe con la "...", ... , "..."

print(f"Ciao {nome}, hai {eta} anni.");
print("Ciao", nome, ", hai", eta, "anni.");