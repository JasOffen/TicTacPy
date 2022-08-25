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
    #Print out the current board
    print(modifiedline1)
    print(modifiedline2)
    print(modifiedline3)

    currentMove = input('Make your move! (ex: 1,2): ')
    if currentMove == "q":
        quit()
    #checks for empty send and restarts the turn
    if currentMove == "":
        print('Please make a move')
        game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
    #line 1 board changes and overlap checks
    if currentMove[2] == '1':
        if currentMove[0] == '1':
            if modifiedline1[0] == 'x' or modifiedline1[0] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline1 = (playingpiece + modifiedline1[1:5])
        if currentMove[0] == '2':
            if modifiedline1[2] == 'x' or modifiedline1[2] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline1 = (modifiedline1[0:2] + playingpiece + modifiedline1[3:5])
                print()
        if currentMove[0] == '3':
            if modifiedline1[4] == 'x' or modifiedline1[4] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline1 = (modifiedline1[0:4] + playingpiece)

    #line 2 board changes and overlap checks
    if currentMove[2] == '2':
        if currentMove[0] == '1':
            if modifiedline2[0] == 'x' or modifiedline2[0] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline2 = (playingpiece + modifiedline2[1:5])
        if currentMove[0] == '2':
            if modifiedline2[2] == 'x' or modifiedline2[2] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline2 = (modifiedline2[0:2] + playingpiece + modifiedline2[3:5])
        if currentMove[0] == '3':
            if modifiedline2[4] == 'x' or modifiedline2[4] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline2 = (modifiedline2[0:4] + playingpiece)

    #line 3 board changes and overlap checks
    if currentMove[2] == '3':
        if currentMove[0] == '1':
            if modifiedline3[0] == 'x' or modifiedline3[0] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline3 = (playingpiece + modifiedline3[1:5])
        if currentMove[0] == '2':
            if modifiedline3[2] == 'x' or modifiedline3[2] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline3 = (modifiedline3[0:2] + playingpiece + modifiedline3[3:5])
        if currentMove[0] == '3':
            if modifiedline3[4] == 'x' or modifiedline3[4] == 'o':
                print("Please pick another spot")
                game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)
            else:
                modifiedline3 = (modifiedline3[0:4] + playingpiece)

    #Three in a row check

    #Flips it to the next players turn
    if is_x == True:
        is_x = False
    else:
        is_x = True

    game_loop(modifiedline1, modifiedline2, modifiedline3, is_x)

game_loop(line1, line2, line3, is_X)
