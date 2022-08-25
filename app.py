import string

def game_loop():
    print('_|_|_')
    print('_|_|_')
    print('_|_|_')
    currentMove = input('Make your move! (ex: 1,2): ')
    print(currentMove)
    game_loop()

game_loop()
