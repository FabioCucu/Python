import socket
import tkinter as tk
from tkinter import messagebox

# Inizializzazione lato client della socket su porta 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Realizzazione interfaccia di prenotazione
def prenotazioneInterface():
    # Assegnazione del contenuto delle box di testo
    partenza = entry_partenza.get()
    arrivo = entry_arrivo.get()
    
    # Controllo che entrambi i campi siano compilati
    if not partenza or not arrivo:
        # Dovessero essere vuoti, mostro un errore
        messagebox.showerror("Errore", "Inserisci sia città di partenza che di arrivo")
        return
    
    # Creazione messaggio nel formato "partenza|arrivo"
    messaggio = f"{partenza}|{arrivo}"
    
    # Invio del messaggio al server sotto forma di sequenza di byte
    client_socket.sendall(messaggio.encode())
    
    # Ricezione risposta server e decodifica
    response = client_socket.recv(1024).decode()
    
    # Mostro su schermo in un message box la risposta del server
    messagebox.showinfo("Risposta dalla centrale", response)
    
    client_socket.close()
    root.destroy()

# Inizializzazione finestra (tk.Tk()) nella variabile root
root = tk.Tk()
# Assegnazione titolo alla finestra
root.title("Prenotazione Taxi")

# Creazione testo di sottotitolo per città di partenza (Label) all'interno della finestra
label_partenza = tk.Label(root, text="Inserisci città di partenza")  # 1° arg:Finestra in cui va il testo, 2° arg: Il testo stesso
# Regolazione posizione del label con padding verticale (pady) di 5
label_partenza.pack(pady=5)

# Creazione box di testo (Entry) per inserimento città di partenza all'interno della finestra
entry_partenza = tk.Entry(root)  # 1° arg:Finestra in cui va la box di testo
# Regolazione posizione della message box con padding verticale (pady) di 5
entry_partenza.pack(pady=5)

# Creazione testo di sottotitolo per città di arrivo (Label) all'interno della finestra
label_arrivo = tk.Label(root, text="Inserisci città di arrivo")  # 1° arg:Finestra in cui va il testo, 2° arg: Il testo stesso
# Regolazione posizione del label con padding verticale (pady) di 5
label_arrivo.pack(pady=5)

# Creazione box di testo (Entry) per inserimento città di arrivo all'interno della finestra
entry_arrivo = tk.Entry(root)  # 1° arg:Finestra in cui va la box di testo
# Regolazione posizione della message box con padding verticale (pady) di 5
entry_arrivo.pack(pady=5)

# Creazione bottone (Button) per invio prenotazione all'interno della finestra
button = tk.Button(root, text="Prenota", command=prenotazioneInterface)
# Regolazione posizione del bottone con padding verticale (pady) di 10
button.pack(pady=10)

# Inizializzazione loop principale di Tkinter che tiene aperta la finestra e attende il click del bottone
root.mainloop()