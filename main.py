    #import
import time
import os
print("benvenuto nel calcolatore autmatico dell'MCD")
print("versione 0.0.1")
time.sleep(1)
cor = input("se vuoi che il programma non si chiuda dopo aver restituito il risultato, scrivi 'ok', altrimenti premi invio... ")
print("per prima cosa inseriamo i numeri di cui vuoi calcolare l'MCD")

def principale(): #definisco la funzione principale. Essa contiene tutto il codice necessario al funzionamento del programma. Mi serve solo per essere richiamate nel caso di inserimento di numeri non supportati
    while True:
        #definizione varibili
        aa1 = input('inserisci il primo numero  ')
        bb1 = input('inserisci il secondo numero  ')
        #valido le variabili e controllo se sono numeri supportati
        try:
            a1 = int(aa1)  #tentativo di conversione in intero n1
            b1 = int(bb1)  #tentativo di conversione in intero n2
        except ValueError: #se si verifica l'eccezione valuerrror (errore di conversione)
            print('sono ammessi solamente numeri interi, quindi senza virgola, punto, lettere o altri caratteri al di fuori di nuemri ') #stampo l'alert
            principale() #faccio ripartire il programma
        a = a1
        b = b1
        print('grazie! ora eseguo i calcoli')
        
        #algoritmo
        while a != b:
            if a > b :
                a = a-b
            if b > a :
                b = b-a
        
        time.sleep(2)
        print("ho finito!")
        print("L'MCD tra " + str(a1) + " e " + str(b1) + " è: " + str(a))

        if cor != 'ok':
            break
principale()
input('premi invio per uscire')
