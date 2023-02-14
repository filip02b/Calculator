while True:
    decizie = input("Tastati 'start' pentru a porni calculatorul sau 'quit' pentru a iesi.").upper()        # Utilizatorul alege sa porneasca sau sa opreasca aplicatia (indiferent cum este scris cuvantul cheie)
    if decizie == 'START':                                                                                  # Conditia de pornire a aplicatiei
        m = input("m: ")
        n = input("n: ")
        if not m.isnumeric() or not n.isnumeric():
            print("Invalid data. Insert numeric values")
            exit()
        m = float(m)
        n = float(n)
        operand = input("Alegeti un operand (+, -, /, *, ^): ")                                             # Operatorul alege operandul
        numere = [m, n]                                                                                     # Numerele instructiunii se salveaza intr-o lista
        if operand == '+':                                                                                  # Conditia de adunare daca operatorul alege operandul "+"
            rezultat = float(numere[0]) + float(numere[1])
        elif operand == '-':                                                                                # Conditia de scadere daca operatorul alege operandul "-"
            rezultat = float(numere[0]) - float(numere[1])
        elif operand == '/':                                                                                # Conditia de impartire daca operatorul alege operandul "/"
            rezultat = float(numere[0]) / float(numere[1])
        elif operand == '*':                                                                                # Conditia de inmultire daca operatorul alege operandul "*"
            rezultat = float(numere[0]) * float(numere[1])
        elif operand == '^':                                                                                # Conditia de ridicat la putere daca operatorul alege operandul "*"
            rezultat = float(numere[0]) ** float(numere[1])
        print(f"{m} {operand} {n}", " = ", rezultat)                                                        # Afisarea rezultatului 
    elif decizie == 'QUIT':                                                                                 # Conditia de oprire a aplicatiei
        exit()
     