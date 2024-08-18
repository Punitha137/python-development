
board = [' ' for _ in range(9)]
player = 'X'

def display_board():
  
  for i in range(3):
    print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')

def is_winner(mark):
  
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
      return True
  return False

def is_board_full():
  
  for space in board:
    if space == ' ':
      return False
  return True

def player_move(mark):
  
  while True:
    try:
      move = int(input(f"Player {mark}, enter your move (1-9): "))
      if 1 <= move <= 9 and board[move - 1] == ' ':
        return move - 1
      else:
        print("Invalid move. Please choose an empty space (1-9).")
    except ValueError:
      print("Invalid input. Please enter a number.")

def switch_player():
  
  global player
  player = 'O' if player == 'X' else 'X'

def main():
  
  print("Welcome to Tic Tac Toe!")
  display_board()

  while True:
    
    move = player_move(player)

    
    board[move] = player

    
    display_board()

  

    if is_winner(player):
      print(f"Player {player} wins!")
      break
    elif is_board_full():
      print("It's a tie!")
      
      break

    
    switch_player()

if __name__ == "__main__":
  main()
