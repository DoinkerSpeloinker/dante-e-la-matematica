import matplotlib.pyplot as plt

def crea_disposizioni(facce:int) -> list:
    """Crea una lista di disposizioni di 3 elementi con un numero 'facce' di elementi ripetuti"""
    risultato: list = []
    for i in range(1, facce+1):
        for j in range(1, facce+1):
            for k in range(1, facce+1):
                risultato.append([i,j,k])

    return risultato

def somma_elementi(lista:list) -> list:
    """Somma le disposizioni (elementi) di una lista e ritorna una lista con le varie somme"""
    return [sum(n) for n in lista]

def trova_numeri_puri(lista:list) -> list:
    """Prende una lista di somma e trova i vari valori unici che appaiono, ridando una lista come output"""
    return list(set(lista))

def calcola_probabilita(lista_somma:list, lista_numeri:list) -> dict:
    """Calcola le volte cui appaiono e fa la probabilità con le volte totali che sono apparse"""
    risultato: dict = {}

    for n in lista_somma:
        risultato[n] = ( lista_numeri.count(n) / len(lista_numeri) ) * 100

    return risultato

def main() -> None:
    """Funzione principale"""

    while True:
        try:
            facce = int(input("Inserisci il numero di facce: "))
            break
        except Exception as e:
            print("Input invalido!")

    disp: list = crea_disposizioni(facce)
    somma:list = somma_elementi(disp)
    numeri:list = trova_numeri_puri(somma)
    probabilita:dict = calcola_probabilita(numeri, somma)

    for numero in probabilita:
        print(f"{numero} ha una probabilità di {probabilita[numero]}")

    plt.bar([n for n in probabilita], [probabilita[n] for n in probabilita])
    plt.xlabel('Numeri unici')
    plt.ylabel('Probabilità')
    plt.title(f'Probabilità delle somme di 3 dadi con {facce} facce')

    plt.show()

if __name__ == '__main__':
    main()

    while True:
        try:
            print("Ne vuoi fare un altro? (S/N)")
            risp = input("").lower()
            if risp == 's':
                main()
            elif risp == 'n':
                print("Alla prossima!")
                break
            else:
                print("Inserisci una risposta valida!")
        except Exception as e:
            print("Input invalido!")