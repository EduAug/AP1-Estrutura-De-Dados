deck = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

def menu():
    print("""
1- Adicionar no início
2- Adicionar no final
3- Exibir primeiro
4- Exibir último
5- Remover primeiro
6- Remover último
7- Exibir Deck (Opção surpresa)
0- Sair          
          """)

def addFirst(value):
    deck.insert(0,value)

def addLast(value):
    deck.append(value)

def showFirst():
    if deck:
        print(deck[0])
    else:
        print("O deck está vazio, hora de embaralhar a mesa")

def showLast():
    if deck:
        print(deck[-1])
    else:
        print("O deck está vazio, hora de embaralhar a mesa")

def removeFirst():
    if deck:
        deck.pop(0)
    else:
        print("O deck está vazio, hora de embaralhar a mesa")

def removeLast():
    if deck:
        deck.pop()
    else:
        print("O deck está vazio, hora de embaralhar a mesa")

def showDeck(lista):
    print(lista)

while True:
    menu()
    alternativa = input("Escolha uma opção:\t")

    if alternativa == '1':
        addFirst(input("Digite o dado a ser inserido no começo do deck: "))
    elif alternativa == '2':
        addLast(input("Digite o dado a ser inserido no final do deck: "))
    elif alternativa == '3':
        showFirst()
    elif alternativa == '4':
        showLast()
    elif alternativa == '5':
        removeFirst()
    elif alternativa == '6':
        removeLast()
    elif alternativa == '7':
        showDeck(deck)
    elif alternativa == '0':
        break
    else:
        print("Opção não suportada!")