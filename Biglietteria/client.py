import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Inizializzazione socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Dizionario per memorizzare i film ricevuti dal server
films_data = {}

# Funzione per ricevere la lista dei film dal server
def receive_films():
    # Ricezione dati dal server
    data = client_socket.recv(1024).decode()
    
    # Parsing dei dati: film1|biglietti|prezzo;film2|biglietti|prezzo;...
    film_entries = data.split(";")
    
    for entry in film_entries:
        if entry:  # Verifica che la stringa non sia vuota
            parts = entry.split("|")
            film_name = parts[0]
            tickets_available = int(parts[1])
            price = float(parts[2])
            films_data[film_name] = [tickets_available, price]
    
    # Popola il menu a tendina con i nomi dei film
    film_names = list(films_data.keys())
    film_combo['values'] = film_names
    if film_names:
        film_combo.current(0)  # Seleziona il primo film
        update_film_info()

# Funzione per aggiornare le informazioni del film selezionato
def update_film_info(event=None):
    selected_film = film_combo.get()
    if selected_film in films_data:
        tickets_available = films_data[selected_film][0]
        price = films_data[selected_film][1]
        info_label.config(text=f"Biglietti disponibili: {tickets_available} - Prezzo: €{price:.2f}")

# Funzione per l'acquisto dei biglietti
def buy_tickets():
    selected_film = film_combo.get()
    num_tickets_str = entry_tickets.get()
    
    # Controllo che il numero di biglietti sia valido
    if not num_tickets_str.isdigit():
        messagebox.showerror("Errore", "Inserisci un numero valido di biglietti")
        return
    
    num_tickets = int(num_tickets_str)
    
    # Controllo che il numero sia positivo
    if num_tickets <= 0:
        messagebox.showerror("Errore", "Il numero di biglietti deve essere maggiore di zero")
        return
    
    # Invio richiesta al server
    request = f"{selected_film}|{num_tickets}"
    client_socket.sendall(request.encode())
    
    # Ricezione risposta dal server
    response = client_socket.recv(1024).decode()
    
    # Parsing della risposta
    parts = response.split("|")
    
    if parts[0] == "OK":
        total_price = parts[1]
        discount_percent = parts[2]
        discount_amount = parts[3]
        final_price = parts[4]
        
        # Messaggio di conferma
        message = f"Film: {selected_film}\n"
        message += f"Biglietti: {num_tickets}\n"
        message += f"Prezzo totale: €{total_price}\n"
        message += f"Sconto: {discount_percent}% (€{discount_amount})\n"
        message += f"Importo finale: €{final_price}"
        
        messagebox.showinfo("Acquisto completato", message)
        
        # Chiusura della finestra e della connessione
        client_socket.close()
        root.destroy()
    else:
        # Errore dal server
        error_message = parts[1]
        messagebox.showerror("Errore", error_message)
    
    # Svuota la casella di testo
    entry_tickets.delete(0, tk.END)

# Creazione finestra principale
root = tk.Tk()
root.title("Biglietteria Cinema")

# Label titolo
title_label = tk.Label(root, text="Seleziona il film", font=("Arial", 12))
title_label.pack(pady=10)

# Menu a tendina per la selezione del film
film_combo = ttk.Combobox(root, state="readonly", width=30)
film_combo.pack(pady=5)
film_combo.bind("<<ComboboxSelected>>", update_film_info)

# Label per mostrare informazioni sul film selezionato
info_label = tk.Label(root, text="")
info_label.pack(pady=5)

# Label per il numero di biglietti
tickets_label = tk.Label(root, text="Numero di biglietti:")
tickets_label.pack(pady=5)

# Entry per inserire il numero di biglietti
entry_tickets = tk.Entry(root)
entry_tickets.pack(pady=5)

# Bottone per l'acquisto
buy_button = tk.Button(root, text="Acquista", command=buy_tickets)
buy_button.pack(pady=10)

# Ricezione lista film dal server
receive_films()

# Avvio del loop principale
root.mainloop()