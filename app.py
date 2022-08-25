import string
line1 = ('_|_|_')
line2 = ('_|_|_')
line3 = ('_|_|_')
is_X = True

def game_loop(modifiedline1, modifiedline2, modifiedline3, is_x):

    if is_x == True:
        playingpiece = 'x'
    else:
        playingpiece = 'o'

    print(modifiedline1)
    print(modifiedline2)
    print(modifiedline3)

    currentMove = input('Make your move! (ex: 1,2): ')
    if currentMove == "q":
        quit()
    if currentMove == "":
        print('Please make a move')
        game_loop()
    if currentMove[2] == '1':
        if currentMove[0] == '1':
            modifiedline1 = (playingpiece + modifiedline1[1:5])
        if currentMove[0] == '2':
            modifiedline1 = (modifiedline1[0:2] + playingpiece + modifiedline1[3:5])
        if currentMove[0] == '3':
            modifiedline1 = (modifiedline1[0:4] + playingpiece)

    if is_x == True:
        is_x = False
    else:
        is_x = True
        
    game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)

game_loop(line1, line2, line3, is_X)
