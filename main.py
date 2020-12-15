import random as rnd

"""ВЫВОД ПОЛЯ"""
def showPlayBoard(board):
    for i in range(3):
      print(board[i])

"""ОРГАНИЗАЦИЯ ОЧЕРЕДИ ХОДА"""
def showTurn(turn, player1, player2):
    if turn == 0:
        print("Ход игрока: ", str(player1))
    else:
        print("Ход игрока: ", str(player2))
    print("Введите номер ячейки")

"""СОЗДАНИЕ МЕТКИ НА ПОЛЕ"""
def choice(turn, playerChoice, board):
    if turn == 0:
        for i in range(3):
            for j in range(3):
                if board[i][j] == int(playerChoice):
                    board[i][j] = "X"
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == int(playerChoice):
                    board[i][j] = "O"



"""ИНИЦИАЛИЗАЦИЯ"""
print("Введите имя игрока")
player1 = input()
print("Введите имя оппонента")
player2 = input()
print(player1 + " VS " + player2)

"""СБРАСЫВАЕМ ПОЛЕ"""
def restartBoard():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return board

"""Определение первого игрока"""
def firstPlayer():
    flipcoin = rnd.randrange(0,2)
    turn = flipcoin
    pl1 = player1
    pl2 = player2
    if(flipcoin == 0):
        print(str(player1) + " играет за (X), " + str(player2) + " играет за (O)")
    else:
        print(str(player1) + " играет за (O), " + str(player2) + " играет за (X)")
        pl1 = player2
        pl2 = player1
        turn = 0
    return turn, pl1, pl2

win1 = ['X','X','X']
win2 = ['O','O','O']

def WinCheck(board):
    """ГОРИЗОНТАЛЬНЫЕ"""
    if(board[0] == win1 or board[0] == win2):
        return 1
    if (board[1] == win1 or board[1] == win2):
        return 1
    if (board[2] == win1 or board[2] == win2):
        return 1

    """ВЕРТИКАЛЬНЫЕ"""
    Y1 = [board[0][0], board[1][0], board[2][0]]
    Y2 = [board[0][1], board[1][1], board[2][1]]
    Y3 = [board[0][2], board[1][2], board[2][2]]
    if (Y1 == win1 or Y1 == win2):
        return 1
    if (Y2 == win1 or Y2 == win2):
        return 1
    if (Y3 == win1 or Y3 == win2):
        return 1

    """КРЕСТ"""
    X1 = [board[0][0], board[1][1], board[2][2]]
    X2 = [board[2][0], board[1][1], board[0][2]]
    if (X1 == win1 or X1 == win2):
        return 1
    if (X2 == win1 or X2 == win2):
        return 1


"""НАЧАЛО ИГРЫ"""
def Game():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    turnCount = 0
    turn, player1, player2 = firstPlayer()
    print(player1, player2)
    isEnd = False
    while(isEnd == False and turnCount<9):
        """Переменная, отвечающая за проверку ячейки на игровом поле"""
        itsOk = False
        showPlayBoard(board)
        showTurn(turn, player1, player2)
        while True:
            """Проверка на корректность ввода"""
            playerChoice = input()
            if (str(playerChoice).upper() == "RESTART"):
                break
            for i in range(3):
                for j in range(3):
                    if str(board[i][j]) == playerChoice:
                        itsOk = True
            if itsOk:
                break
        if(str(playerChoice).upper() == "RESTART"):
            Game()
        choice(turn, playerChoice, board)
        if turn == 1:
            turn = 0
        else:
            turn = 1
        turnCount = turnCount + 1
        if (WinCheck(board) == 1):
            isEnd = True
            if(turn == 1):
                print("Победил игрок: " + player1)
            else: print("Победил игрок: " + player2)
    if turnCount == 9 or isEnd == True:
        print("Введите restart, чтобы начать заново")
        playerChoice = input()
        if (str(playerChoice).upper() == "RESTART"):
            Game()


Game()
#
# print(board[1][1])
# """5"""
#
