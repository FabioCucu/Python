import socket

def start_client():
    # Inizializzazione lato client della socket su porta 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    # Realizzazione logica di prenotazione
    # Inserimento città di partenza
    partenza = input("Inserisci città di partenza: ")
    # Inserimento città di arrivo
    arrivo = input("Inserisci città di arrivo: ")
    
    # Creazione messaggio nel formato "partenza|arrivo"
    messaggio = f"{partenza}|{arrivo}"
    
    # Invio il messaggio sotto forma di sequenza di byte (encode())
    client_socket.sendall(messaggio.encode())
    
    # Ricezione risposta server e decodifica della sequenza di byte (decode())
    data = client_socket.recv(1024).decode()
    
    # Presentazione su schermo della risposta ricevuta
    print(data)
    
    # Chiusura connessione del client
    client_socket.close()

# Chiamata della funzione 'start_client' in main
if __name__ == "__main__":
    start_client()
