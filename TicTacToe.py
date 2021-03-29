

def printBoard(B):
    print(B[7]+' | '+B[8]+' | '+B[9])
    print('---------')
    print(B[4]+' | '+B[5]+' | '+B[6])
    print('---------')
    print(B[1]+' | '+B[2]+' | '+B[3])
    
def isWinner(B):
    return (B[1]==B[2] and B[1]==B[3] and B[1] != ' ')or(B[4]==B[5] and B[4]==B[6]and B[4] != ' ')or(B[7]==B[8] and B[7]==B[9]and B[9] != ' ')or(B[1]==B[4] and B[1]==B[7]and B[7] != ' ')or(B[2]==B[5] and B[2]==B[8]and B[2] != ' ')or(B[3]==B[6] and B[3]==B[9]and B[9] != ' ')or(B[1]==B[5] and B[1]==B[9]and B[9] != ' ')or(B[3]==B[5] and B[3]==B[7]and B[3] != ' ')

def isFull(B):
    return not B.count(' ') > 1

def move(A,B,p):
    print('Select', p, 'Position from 1 through 9 : ',end = ' ')
    x = int(input())
    print('\n')
    if x in A and B[x] == ' ':
        B[x] = p
    else :
        print('Enter a valid position')
        printBoard(B)
        move(A,B,p)
    return B
    
while True :
    B = []
    for i in range(10):
        B.append(' ')
    
    A = [1,2,3,4,5,6,7,8,9]
    
    while True:
    
        printBoard(B)
        
        move(A,B,'X')
            
        printBoard(B)
        
        if isWinner(B) :
            print ("'X' is the winner!")
            break
        
        if isFull(B):
            print('Tie Game!')
            break
               
        move(A,B, 'O')
        
        if isWinner(B) :
            printBoard(B)
            print ("'O' is the winner!")
            break
        
        if isFull(B):
            print('Tie Game!')
            break
    inp = int(input('Press 1 to play again and anyother key to exit : '))
    if inp != 1:
        break
print('Thank You!!')
