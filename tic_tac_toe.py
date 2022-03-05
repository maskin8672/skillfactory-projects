the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


turn = 'X'


def win():
    return the_board['top-L'] == the_board['top-M'] == the_board['top-R'] == turn or \
           the_board['mid-L'] == the_board['mid-M'] == the_board['mid-R'] == turn or \
           the_board['low-L'] == the_board['low-M'] == the_board['low-R'] == turn or \
           the_board['top-L'] == the_board['mid-L'] == the_board['low-L'] == turn or \
           the_board['top-M'] == the_board['mid-M'] == the_board['low-M'] == turn or \
           the_board['top-R'] == the_board['mid-R'] == the_board['low-R'] == turn or \
           the_board['top-L'] == the_board['mid-M'] == the_board['low-R'] == turn or \
           the_board['top-R'] == the_board['mid-M'] == the_board['low-L'] == turn


def draw():
    return ' ' in the_board.values() 
           

def print_board(board):
    print('     ', board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('     ', '-+-+-')
    print('     ', board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('     ', '-+-+-')
    print('     ', board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print()


def main():
    global turn
    for i in range(9):
        print('''---------------------------------------------------
  Enter the position name for X/O placement:
     top-L | top-M | top-R
     +++++++++++++++++++++
     mid-L | mid-M | mid-R
     +++++++++++++++++++++
     low-L | mid-M | mid-R
---------------------------------------------------
        ''')
        print_board(the_board)
        print('  Turn for ' + turn + '. Move on wich space: ', end='')
        move = input()
        the_board[move] = turn
        if win():
            print()
            print_board(the_board)
            print('  You win!')
            break
        if not draw():
            print()
            print_board(the_board)
            print('  Friendship won!')
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


if __name__ == '__main__':
    main()
