import socket
import threading

# Variabile globale per la disponibilità dei taxi
taxi_disponibili = 10

# Definizione funzione istanza di prenotazione
def prenotazioneInstance(conn, addr):
    global taxi_disponibili
    print(f"Connessione stabilita con {addr}")
    
    # Loop che riceve le richieste di prenotazione
    while True:
        # Ricezione dati dal client e decodifica
        data = conn.recv(1024).decode()
        
        # Se il client chiude la connessione
        if not data:
            break
            
        # Parsing dei dati ricevuti (formato: "partenza|arrivo")
        try:
            partenza, arrivo = data.split('|')
            
            # Verifica disponibilità taxi
            if taxi_disponibili > 0:
                taxi_disponibili -= 1
                response = f"Prenotazione confermata!\nDa: {partenza}\nA: {arrivo}\nTaxi disponibili rimasti: {taxi_disponibili}"
            else:
                response = "Spiacenti, nessun taxi disponibile al momento."
            
            # Invio risposta come sequenza di byte al client
            conn.send(response.encode())
            
            # Chiudo la connessione dopo aver gestito la prenotazione
            break
            
        except ValueError:
            response = "Errore nel formato dei dati"
            conn.send(response.encode())
            break
    
    # Chiusura connessione con il client
    conn.close()
    print(f"Connessione terminata con {addr}")

def start_server():
    # Inizializzazione lato server della socket su porta 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("Server della centrale taxi in ascolto sulla porta 12345...")
    print(f"Taxi disponibili: {taxi_disponibili}")
    
    # Loop che accetta continuamente le nuove connessioni
    while True:
        conn, addr = server_socket.accept()
        '''Inizializzazione thread(Processo a sè stante che esegue
           la funzione di prenotazione per l'istanza corrente)'''
        client_thread = threading.Thread(
            # target: Funzione che il thread eseguirà
            target=prenotazioneInstance,
            # args: Argomenti che verranno passati alla funzione passata come target
            args=(conn, addr)
        )
        # Avvio del thread
        client_thread.start()

# Chiamata della funzione 'start_server' in main
if __name__ == "__main__":
    start_server()
