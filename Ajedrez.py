def partida_ajedrez(ajedrez):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero=[]
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))

    f = open("ajedrez", 'w')
    for i in partida_ajedrez:
        f.write('\t'.join(i) + '\n')
    f.close()

movimiento = 0

while True:
    seguirjugando = input("Deseas hacer otro movimiento (si/no): ")
    if seguirjugando == "no" :
        break
    else:
        filainicial = int(input("Introduce la fila de la pieza a mover: "))
        columnainicial = int(input("Introduce la columna de la pieza a mover: "))
        filadestino = int(input("Introduce la fila de destino: "))
        columnadestino = int(input("Introduce la columna de destino: "))
        