import random

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print()
    print()
    print()
    print()
    print('The Positions Are:')
    print()
    print('   |   |')
    print(f' 1 | 2 | 3')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' 4 | 5 | 6')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' 7 | 8 | 9')
    print('   |   |')

    print()
    print()
    print()
    print('Your Board:')
    print()
    print('   |   |')
    print(f' {board[1]} | {board[2]} | {board[3]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[4]} | {board[5]} | {board[6]}')
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(f' {board[7]} | {board[8]} | {board[9]}')
    print('   |   |')


def isWinner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[6] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[7] == letter)


def playerMove():
    run = True
    while run:
        move = input("Please Select A Position To Place An 'X' (1 - 9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, This Space Is Occupied!')
            else:
                print('PLease Type A Number Within The Range!')
        except:
            print('Please Type A Number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(list):
    listLen = len(list)
    randNo = random.randrange(0, listLen)
    return list[randNo]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print('Welcome To Tic Tac Toe Game! Created By Programmer Snigdho')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O/Computer Won This Time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('The Game Is Tie!')
            else:
                insertLetter('O', move)
                print(f"Computer Placed An 'O' In Position: {move}")
                printBoard(board)
        else:
            print('Congratulations! X/You Won This Time!')
            break

    if isBoardFull(board):
        print('The Game Is Tie!')

main()
while True:
    answer = input("Do You Want To Play It Again? (Y/N)")
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
