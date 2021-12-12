def partida_ajedrez(ajedrez):
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    tablero=[]
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))

    f = open("ajedrez", 'w')
    for i in partida_ajedrez:
        f.write('\t'.join(i) + '\n')
    f.close()
    