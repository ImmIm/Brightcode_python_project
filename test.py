import os




def draw_board(size):
    board_size = size
    header = '-' * (4 * board_size + 1)
    print(header)
    for i in range(board_size):
      for j in range(board_size):
        cell = ' '
        print(f'| {cell} ', end='')
      print('|')
    print(header)


draw_board(8)
os.system('CLS')


draw_board(8)

