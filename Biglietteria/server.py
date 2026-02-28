import socket
import threading

'''
# films => nome, biglietti disponibili, prezzo,...
films = ["Avatar", 50, 8.50, "Inception", 30, 7.00, "Interstellar", 40, 7.50, "The Matrix", 25, 6.50]
'''

films = {
    "Avatar": [50, 8.50],
    "Inception": [30, 7.00],
    "Interstellar": [40, 7.50],
    "The Matrix": [25, 6.50]
}

# Funzione per calcolare lo sconto in base al numero di biglietti
def calculate_discount(num_tickets):
    if num_tickets >= 5:
        return 0.20  # 20% di sconto per 5 o più biglietti in decimale
    elif num_tickets >= 3:
        return 0.10  # 10% di sconto per 3-4 biglietti in decimale
    else:
        return 0.0   # Nessuno sconto, compra di piu', tirchio

# Funzione per gestire la connessione con un singolo client
def handle_client(conn, addr):
    print(f"Connessione stabilita con {addr}")
    
    # Preparazione lista film da inviare al client
    film_list = ""
    for film_name, film_data in films.items():
        film_list += f"{film_name}|{film_data[0]}|{film_data[1]};"
    
    # Invio lista film al client
    conn.send(film_list.encode())
    
    # Ricezione richiesta dal client
    data = conn.recv(1024).decode()
    
    # Parsing dei dati ricevuti: film_name|num_tickets
    parts = data.split("|")
    selected_film = parts[0]
    num_tickets = int(parts[1])
    
    # Verifica disponibilità biglietti
    if selected_film in films:
        available_tickets = films[selected_film][0] # films[selected_film => "Avatar"][0 => 50]
        ticket_price = films[selected_film][1] 
        
        if num_tickets > available_tickets:
            # Biglietti non disponibili
            response = f"ERRORE|Non ci sono abbastanza biglietti disponibili"
        else:
            # Calcolo prezzo totale
            total_price = ticket_price * num_tickets
            
            # Calcolo sconto
            discount_percentage = calculate_discount(num_tickets)
            discount_amount = total_price * discount_percentage
            
            # Prezzo finale
            final_price = total_price - discount_amount
            
            # Invio risposta al client
            response = f"OK|{total_price:.2f}|{discount_percentage*100:.0f}|{discount_amount:.2f}|{final_price:.2f}"
    else:
        response = "ERRORE|Film non trovato"
    
    conn.send(response.encode())
    
    # Chiusura connessione
    conn.close()
    print(f"Connessione terminata con {addr}")

# Funzione principale del server
def start_server():
    # Inizializzazione socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server biglietteria in ascolto sulla porta 12345...")
    
    # Loop per accettare connessioni 
    while True:
        conn, addr = server_socket.accept()
        # Creazione thread per gestire il client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

# Avvio del server
if __name__ == "__main__":
    start_server()