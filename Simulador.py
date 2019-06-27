# -*- encoding = utf8 -*-

import time
import logging
import datetime

logging.basicConfig(format='%(asctime)s %(name)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='Log.txt')
logging.warning('Iniciou o programa')

filaDeVoos = ['AFR447','JAL123','GOL1907','TAM3054','MH370']
pista = []
tamanhoPista = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pistaPronta = pista + tamanhoPista

#Simulação de pouso
def pouso():
    logging.warning('Iniciou o simulador de pouso')
    voo = input("Escreva o código do seu voo:")
    print("Seu voo é:",voo)
    print("Preparando pista para pouso!")
    voo = '+'
    pistaPronta[0] = voo
    pousar = input("Aperte 'p' para fazer o pouso")
    if pouso == ("p"):
        percorrer(pistaPronta)
    print("Pouso efetuado com sucesso!")
    logging.warning('Pouso efetuado com sucesso')
    logging.warning('Pista livre')

#Simulação de decolagem
def decolagem():
    logging.warning('Iniciou o simulador de decolagem')
    print("Fila de Decolagem:", filaDeVoos)
    pista.append(filaDeVoos[0])
    filaDeVoos.pop(0)
    pistaPronta[0] = '+'
    print(pistaPronta)
    decolar = input("Aperte 's' para iniciar decolagem.\n")
    if decolar == ("s"):
        logging.warning('O  avião entrou na pista para decolagem')
        print("Aguarde 10 segundos para a decolagem.")
        time.sleep(10)
        percorrer(pistaPronta)
        print("Decolagem efetuada com sucesso!")
        logging.warning('Voo decolado com sucesso')
        logging.warning('Pista livre')

def percorrer(pistaPronta):
    logging.warning('Pista em uso')
    print("Pista:", pistaPronta)
    for i in range (len(pistaPronta)-1):
        pistaPronta[i+1] = pistaPronta[i]
        pistaPronta[i] = 0
        print("Pista:", pistaPronta)
    pistaPronta[i+1] = 0
    print("Pista:", pistaPronta)
        

#Menu de início
print("Simulador de Aeroporto")
iniciar = input("Escolha a Simulação que deseja fazer.\na) Decolagem\nb) Pouso\n")
if iniciar == ("a"):
    decolagem()
elif iniciar == ("b"):
    pouso()
else:
    print("Simulador sendo desligado")
