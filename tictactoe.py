def printBoard(board):
    index = 0
    colMarker = "ABC"
    i = 0
    while i < 4:
        if i == 0:
            print " ",
            i = i+1;
            continue;
        else:
            print colMarker[i-1],
            i = i+1
    print
    i = 1
    pos = 0
    while i < 4:
        print i,
        for pos in xrange(pos, pos+3):
            print board[i-1][pos],
            
        pos = 0
        i = i+1
        print 
        
def placeX(s, board):
    s = s.lower()
    col = ord(s[0])-97
    row =  int(s[1])-1
    board[row][col] = 'X'
            
def placeO(s, board):
    s = s.lower()
    col = ord(s[0])-97
    row =  int(s[1])-1
    board[row][col] = 'O'  
            
def checkWin(s, board):
    if((board[0][0] == s and board[0][0] == board[0][1] and board[0][1]==board[0][2]) or 
    (board[1][0] == s and board[1][1] == board[1][0] and board [1][2] == board[1][1]) or 
    (board[2][0] == s and board[2][1] == board[2][0] and board [2][2] == board[2][1]) or
    (board[0][0] == s and board[1][0] == board[0][0] and board[2][0] == board[1][0]) or
    (board[0][1]== s and board[1][1] == board[0][1] and board [2][1]== board[1][1]) or
    (board[0][2] == s and board[1][2] == board[0][2] and board[2][2]==board[1][2]) or
    (board[0][0] == s and board[1][1] == board[0][0] and board[2][2] == board[1][1]) or
    (board[0][2] == s and board[1][1] == board[0][2] and board[2][0] == board[1][1])):
        print "%s wins!" %(s)
        return True
        
def inputIsFalse(s, board):
    s = s.lower()
    col = ord(s[0])-97
    row =  int(s[1])-1
    if((s[0] < 'a' or  s[0] > 'c') or (s[1] < '1' or s[1] > '3')):
        print s[0]
        print s[1]
        return True
    elif (board[row][col] != '-'):
        return True
    else:
        return False
    
def gameDriver():
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    printBoard(board)
    for i in xrange(5):
        response = raw_input("Select X position: ")
        while(inputIsFalse(response, board)):
            response = raw_input("Select X position: ")
            
        placeX(response, board)    
        printBoard(board)
        if(checkWin('X',board)):
            break
        
        
        response = raw_input("Select O position: ")
        while(inputIsFalse(response, board)):
            response = raw_input("Select O position: ")
            
        placeO(response, board)    
        printBoard(board)
        if(checkWin('O',board)):
            break
            
    print "Draw"
    
gameDriver()
