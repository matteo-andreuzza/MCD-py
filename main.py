#import
import time
import os
print("benvenuto nel calcolatore autmatico dell'MCD")
print("versione 0.0.1")
time.sleep(1)
cor = input("se vuoi che il programma non si chiuda dopo aver restituito il risultato, scrivi 'ok', altrimenti premi invio")
print("per prima cosa inseriamo i numeri di cui vuoi calcolare l'MCD")
while True:
    #definizione varibili
    a1 = int(input('inserisci il primo numero  '))
    b1 = int(input('inserisci il secondo numero  '))
    a = a1
    b = b1
    print('grazie! ora eseguo i calcoli')
    time.sleep(1)
    
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
input('premi invio per uscire')