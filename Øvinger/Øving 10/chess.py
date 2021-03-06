class Piece:
  def __init__(self, side, position_x, position_y):
    self.is_white = side.lower() == 'white'
    self.is_alive = True
    self.y = position_y
    self.x = position_x
  
  def is_opposite_piece_at(self, x, y, board_instance) -> bool:
    """Returns 'if it is an opposing piece at x, y or not'"""
    if x<=8 and x>0 and y<=8 and y>0:
      piece = board_instance.get_piece_at(x, y)
      if piece != None:
        return piece.is_white != self.is_white
      else:
        return False
    else:
        return False
  
  def __str__(self):
    """Returns string wth class name"""
    return str(type(self))[17: -2]

class Pawn(Piece):
  def possible_moves(self, board_instance):
    """Return list of possible moves for piece
    (moves in movementpattern that either lands on an open spot or opponents piece)"""
    possible_moves = []
    x = self.x
    y = self.y
    
    def is_in_start_position():
      """Check if pawn is in start postion"""
      if self.is_white:
        return self.y == 2
      else:
        return self.y == 7
    
    def y_change(y, change):
      """Adds or subtracts num from y, depending on witch color it is"""
      if self.is_white:
        return y + change
      else:
        return y - change
    
    if board_instance.get_piece_at(x, y_change(y, 1)) == None:
      possible_moves.append((x, y_change(y, 1)))
      
      if is_in_start_position() and board_instance.get_piece_at(x, y_change(y, 2)) == None:
        possible_moves.append((x, y_change(y, 2)))
    
    if self.is_opposite_piece_at(x + 1, y_change(y, 1), board_instance):
      possible_moves.append((x + 1, y_change(y, 1)))
    
    if self.is_opposite_piece_at(x - 1, y_change(y, 1), board_instance):
      possible_moves.append((x - 1, y_change(y, 1)))
    return possible_moves

class Rook(Piece):
  def possible_moves(self, board_instance):
    """Return list of possible moves for piece
    (moves in movementpattern that either lands on an open spot or opponents piece)"""
    possible_moves = []
    x = self.x
    y = self.y
    
    def search_straight(i, maintained_side):
      """uses y and x from piece and searches in a spot, determined by i and maintained_side,
      it gives back a true or false, dependent on if the search has hit a piece. 
      It also appends moves to possible_moves if the spot is empty or has an enemy piece"""
      if maintained_side == 'y':
        search = i, y
      elif maintained_side == 'x':
        search = x, i
      
      search_piece = board_instance.get_piece_at(*search)
      if search_piece == None:
        possible_moves.append(search)
        return False
      elif self.is_opposite_piece_at(*search, board_instance):
        possible_moves.append(search)
        return True
      else:
        return True
    
    for i in reversed(range(1, x)):
      if search_straight(i, 'y'):
        break    
    for i in range(x + 1, 9 - x):
      if search_straight(i, 'y'):
        break    
    for i in reversed(range(1, y)):
      if search_straight(i, 'x'):
        break
    for i in range(y + 1, 9):
      if search_straight(i, 'x'):
        break
    return possible_moves

class Bishop(Piece):
  def possible_moves(self, board_instance):
    """Return list of possible moves for piece
    (moves in movementpattern that either lands on an open spot or opponents piece)"""
    possible_moves = []
    x = self.x
    y = self.y
    
    def distance_to_edge(dir_x, dir_y):
      """Uses x an y from earlier and checks distance to edge in x and y direction(based on witch way you are looking)
      it gives back smallest distance"""
      if dir_x == '+':
        distance_to_edge_x = 9 - x
      elif dir_x == '-':
        distance_to_edge_x = x
      
      if dir_y == '+':
        distance_to_edge_y = 9 - y      
      elif dir_y == '-':
        distance_to_edge_y = y
      
      if distance_to_edge_x > distance_to_edge_y:
        return distance_to_edge_y
      
      elif distance_to_edge_x <= distance_to_edge_y:
        return distance_to_edge_x
      
    def search(i, dir_x, dir_y):
      """Uses x and y from earlier, takes in modifier (i) and direction for x and y, 
      and gives out a tuple of modified x and y"""
      if dir_x == '+':
        new_x = x + i
      elif dir_x == '-':
        new_x = x - i
      
      if dir_y == '+':
        new_y = y + i
      elif dir_y == '-':
        new_y = y - i
      return new_x, new_y
    
    def diagonal_search(dir_x, dir_y):
      """Takes in witch diagonal (combination of x and y direction) you want to search,
      and adds positions to the possible_moves list"""
      for i in range(1, distance_to_edge(dir_x, dir_y)):
        search_spot = search(i, dir_x, dir_y)
        search_piece = board_instance.get_piece_at(*search_spot)
        if search_piece == None:
          possible_moves.append(search_spot)
        elif self.is_opposite_piece_at(*search_spot, board_instance):
          possible_moves.append(search_spot)
          break
        else:
          break
    
    diagonal_search('+', '+')
    diagonal_search('+', '-')
    diagonal_search('-', '+')
    diagonal_search('-', '-')
    return possible_moves

class Queen(Piece):
  def possible_moves(self, board_instance):
    """Return list of possible moves for piece
    (moves in movementpattern that either lands on an open spot or opponents piece)"""
    possible_moves = []
    x = self.x
    y = self.y
    
    def distance_to_edge(dir_x, dir_y):
      """Uses x an y from earlier and checks distance to edge in x and y direction(based on witch way you are looking)
      it gives back smallest distance"""
      if dir_x == '+':
        distance_to_edge_x = 9 - x
      elif dir_x == '-':
        distance_to_edge_x = x
      
      if dir_y == '+':
        distance_to_edge_y = 9 - y      
      elif dir_y == '-':
        distance_to_edge_y = y
      
      if distance_to_edge_x > distance_to_edge_y:
        return distance_to_edge_y
      
      elif distance_to_edge_x <= distance_to_edge_y:
        return distance_to_edge_x
      
    def search(i, dir_x, dir_y):
      """Uses x and y from earlier, takes in modifier (i) and direction for x and y, 
      and gives out a tuple of modified x and y"""
      if dir_x == '+':
        new_x = x + i
      elif dir_x == '-':
        new_x = x - i
      
      if dir_y == '+':
        new_y = y + i
      elif dir_y == '-':
        new_y = y - i
      return new_x, new_y
    
    def diagonal_search(dir_x, dir_y):
      """Takes in witch diagonal (combination of x and y direction) you want to search,
      and adds positions to the possible_moves list"""
      for i in range(1, distance_to_edge(dir_x, dir_y)):
        search_spot = search(i, dir_x, dir_y)
        search_piece = board_instance.get_piece_at(*search_spot)
        if search_piece == None:
          possible_moves.append(search_spot)
        elif self.is_opposite_piece_at(*search_spot, board_instance):
          possible_moves.append(search_spot)
          break
        else:
          break
    
    diagonal_search('+', '+')
    diagonal_search('+', '-')
    diagonal_search('-', '+')
    diagonal_search('-', '-')
    
    def search_straight(i, maintained_side):
      """uses y and x from piece and searches in a spot, determined by i and maintained_side,
      it gives back a true or false, dependent on if the search has hit a piece. 
      It also appends moves to possible_moves if the spot is empty or has an enemy piece"""
      if maintained_side == 'y':
        search = i, y
      elif maintained_side == 'x':
        search = x, i
      
      search_piece = board_instance.get_piece_at(*search)
      if search_piece == None:
        possible_moves.append(search)
        return False
      elif self.is_opposite_piece_at(*search, board_instance):
        possible_moves.append(search)
        return True
      else:
        return True
    
    for i in reversed(range(1, x)):
      if search_straight(i, 'y'):
        break    
    for i in range(x + 1, 9):
      if search_straight(i, 'y'):
        break    
    for i in reversed(range(1, y)):
      if search_straight(i, 'x'):
        break
    for i in range(y + 1, 9):
      if search_straight(i, 'x'):
        break
    return possible_moves

class Knight(Piece):
  def possible_moves(self, board_instance):
    """Return list of possible moves for piece
    (moves in movementpattern that either lands on an open spot or opponents piece)"""
    possible_moves = []
    x = self.x
    y = self.y
    
    def knight_search(start_x, start_y):
      """Takes in start position and gives out positions for knight that is on the board"""
      move_types = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
      possible_positions = []
      for (x, y) in move_types:
        x_possible = start_x + x
        y_possible = start_y + y
        if 0 < x_possible <= 8 and 0 < y_possible <= 8:
          possible_positions.append((x_possible, y_possible))
      return possible_positions
    searchable_spot = knight_search(x, y)
    
    for search in searchable_spot:
      search_piece = board_instance.get_piece_at(*search)
      if search_piece == None or self.is_opposite_piece_at(*search, board_instance):
        possible_moves.append(search)
    return possible_moves

class King(Piece):
  def possible_moves(self, board_instance):
    """Return list of possible moves for piece
    (moves in movementpattern that either lands on an open spot or opponents piece)"""
    possible_moves = []
    x = self.x
    y = self.y
    
    def king_search(start_x, start_y):
      """Takes in start position and gives out positions for king that is on the board"""
      move_types = [(-1, -1), (-1, 0), (-1, +1), (0, +1), (0, -1), (+1, +1), (+1, 0), (+1, -1)]
      possible_positions = []
      for (x, y) in move_types:
        x_possible = start_x + x
        y_possible = start_y + y
        if 0 < x_possible <= 8 and 0 < y_possible <= 8:
          possible_positions.append((x_possible, y_possible))
      return possible_positions
    searchable_spot = king_search(x, y)
    
    for search in searchable_spot:
      search_piece = board_instance.get_piece_at(*search)
      if search_piece == None or self.is_opposite_piece_at(*search, board_instance):
        possible_moves.append(search)
    
    return possible_moves

class Board:
  def __init__(self):
    self.board=[[Rook('white', 1, 1), Knight('white', 2, 1), Bishop('white', 3, 1), Queen('white', 4, 1), King('white', 5, 1), Bishop('white', 6, 1), Knight('white', 7, 1), Rook('white', 8, 1)],
          [Pawn('white', 1, 2), Pawn('white', 2, 2), Pawn('white', 3, 2), Pawn('white', 4, 2), Pawn('white', 5, 2), Pawn('white', 6, 2), Pawn('white', 7, 2), Pawn('white', 8, 2)], 
          [None, None, None, None, None, None, None, None], 
          [None, None, None, None, None, None, None, None], 
          [None, None, None, None, None, None, None, None], 
          [None, None, None, None, None, None, None, None], 
          [Pawn('black', 1, 7), Pawn('black', 2, 7), Pawn('black', 3, 7), Pawn('black', 4, 7), Pawn('black', 5, 7), Pawn('black', 6, 7), Pawn('black', 7, 7), Pawn('black', 8, 7)], 
          [Rook('black', 1, 8), Knight('black', 2, 8), Bishop('black', 3, 8), Queen('black', 4, 8), King('black', 5, 8), Bishop('black', 6, 8), Knight('black', 7, 8), Rook('black', 8, 8)]]  
  
  def get_piece_at(self, x, y) -> object:
    """Returns piece at the x, y coordinate"""
    return self.board[y-1][x-1]
  
  def draw(self):
    """Prints out the board, in state at the instance it is called"""
    piece_symbols = {'Pawn': ['♙', '♟'], 'Rook': ['♖', '♜'], 'Bishop': ['♗', '♝'], 'Knight': ['♘', '♞'], 'Queen': ['♕', '♛'], 'King': ['♔', '♚']}
    def symbol_at(x, y):
      """Return the symbol for the piece at x, y, returns ' ' for None"""
      piece = self.get_piece_at(x, y)
      if piece == None:
        return ' '
      else:
        return piece_symbols[str(piece)][piece.is_white]

    print(' ┌───┬───┬───┬───┬───┬───┬───┬───┐\n'
        f'8│ {symbol_at(1,8)} │ {symbol_at(2,8)} │ {symbol_at(3,8)} │ {symbol_at(4,8)} │ {symbol_at(5,8)} │ {symbol_at(6,8)} │ {symbol_at(7,8)} │ {symbol_at(8,8)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'7│ {symbol_at(1,7)} │ {symbol_at(2,7)} │ {symbol_at(3,7)} │ {symbol_at(4,7)} │ {symbol_at(5,7)} │ {symbol_at(6,7)} │ {symbol_at(7,7)} │ {symbol_at(8,7)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'6│ {symbol_at(1,6)} │ {symbol_at(2,6)} │ {symbol_at(3,6)} │ {symbol_at(4,6)} │ {symbol_at(5,6)} │ {symbol_at(6,6)} │ {symbol_at(7,6)} │ {symbol_at(8,6)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'5│ {symbol_at(1,5)} │ {symbol_at(2,5)} │ {symbol_at(3,5)} │ {symbol_at(4,5)} │ {symbol_at(5,5)} │ {symbol_at(6,5)} │ {symbol_at(7,5)} │ {symbol_at(8,5)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'4│ {symbol_at(1,4)} │ {symbol_at(2,4)} │ {symbol_at(3,4)} │ {symbol_at(4,4)} │ {symbol_at(5,4)} │ {symbol_at(6,4)} │ {symbol_at(7,4)} │ {symbol_at(8,4)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'3│ {symbol_at(1,3)} │ {symbol_at(2,3)} │ {symbol_at(3,3)} │ {symbol_at(4,3)} │ {symbol_at(5,3)} │ {symbol_at(6,3)} │ {symbol_at(7,3)} │ {symbol_at(8,3)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'2│ {symbol_at(1,2)} │ {symbol_at(2,2)} │ {symbol_at(3,2)} │ {symbol_at(4,2)} │ {symbol_at(5,2)} │ {symbol_at(6,2)} │ {symbol_at(7,2)} │ {symbol_at(8,2)} │\n'
        ' ├───┼───┼───┼───┼───┼───┼───┼───┤\n'
        f'1│ {symbol_at(1,1)} │ {symbol_at(2,1)} │ {symbol_at(3,1)} │ {symbol_at(4,1)} │ {symbol_at(5,1)} │ {symbol_at(6,1)} │ {symbol_at(7,1)} │ {symbol_at(8,1)} │\n'
        ' └───┴───┴───┴───┴───┴───┴───┴───┘\n'
        '   1   2   3   4   5   6   7   8\n')
  
  def promote(self, pawn, y_end):
    """Takes in a pawn object and y after move, asks user what to promote to and
    makes promoted piece where pawn stands"""
    if pawn.is_white:
      end_row = 8
      color = 'white'
    else:
      end_row = 1
      color = 'black'
    x = pawn.x
    y = pawn.y 
    while end_row == y_end:
      new = input('What do you want to promote to? Write the first letter of the piece.\n "K"night, "Q"ueen, "R"ook or "B"ishop: ').upper()
      if new == 'K':
        self.board[y-1][x-1] = Knight(color, x, y)
        break
      elif new == 'Q':
        self.board[y-1][x-1] = Queen(color, x, y)
        break
      elif new == 'R':
        self.board[y-1][x-1] = Rook(color, x, y)
        break
      elif new == 'B':
        self.board[y-1][x-1] = Bishop(color, x, y)
        break
      else:
        print('That is not the first letter of a piece, only write the first letter')
  
  def move(self, start, end):
    """Moves a piece from start to end, and removes opposing piece at end if it is there"""
    piece = self.get_piece_at(*start)
    opposing_piece = self.get_piece_at(*end)
    
    if opposing_piece != None:
      opposing_piece.is_alive = False
      opposing_piece.x = None
      opposing_piece.y = None
    
    if str(piece) == 'Pawn':
      self.promote(piece, end[1])
      piece = self.get_piece_at(*start)
    
    piece.x = end[0]
    piece.y = end[1]
    self.board[start[1]-1][start[0]-1] = None
    self.board[end[1]-1][end[0]-1] = piece
  
  def get_piece_where(self, condition):
    """Returns list of piece-objects where condition apply"""
    result = []
    for row in self.board:
      for piece in row:
        try:
          if condition(piece):
            result.append(piece)
        except Exception:
          pass
    return result
  
  # legal_moves and has_legal_moves
    # def legal_moves(self, piece):
    # """Check all possible moves, and return list of legal moves""" 
    #   lst = piece.possible_moves
    #   start = (piece.x, piece.y)  
    # would include a simulation where it is checked if any of the moves in possible moves
    # leads to own king in check
    
    # def has_legal_moves(self, player_to_check_is_white):
    #   """Check if player has legal moves"""
    #   pieces = get_piece_where(lambda piece: piece != None and piece.is_white == player_to_check_is_white)
    #   legal_moves = [self.legal_moves(piece) for piece in pieces]
    #   return legal_moves == []
  
  def is_in_check(self, player_is_white):
    """Checks if any of the opposite piece can take the king"""
    pieces = self.get_piece_where(lambda piece: piece != None and piece.is_white != player_is_white)
    king = self.get_piece_where(lambda piece: piece != None and piece.is_white == player_is_white and str(piece) == 'King')[0]
    opposite_possible_positions = [piece.possible_moves(self) for piece in pieces]
    king_position = (king.x, king.y)
    # Would use self.legal_moves(piece) instead of piece.possible_moves(self) if it was ready
    return king_position in opposite_possible_positions
  
  # stalemate and checkmate
    # def stale_mate(self, player_to_check_is_white):
    #   """Returns if it is stalemate"""
    #   return has_legal_moves and not is_in_check
    
    # def checkmate_mate(self, player_to_check_is_white):
    #   """Returns if it is checkmate"""
    #   return has_legal_moves and is_in_check

class Game:  
  def __init__(self):
    self.is_done = False
    self.winner = None
    
  def players_color(self, player_is_white):
    if player_is_white:
      return 'White'
    else:
      return 'Black'
    
  def player_move(self, player_to_move):
    if board_instance.is_in_check(player_is_white):
      is_in_check = True
    else:
      is_in_check = False
    
    while True:
      if player_is_white:
        print('White to move')
      else:
        print('Black to move')
      
      board_instance.draw()
      print('To give up, or admit loss write "L", to ask for remiss write "R"')
      if is_in_check:
        print('YOU ARE IN CHECK')
      
      start = input('Give x-coordinate of piece you want to move: ')
      if start == 'L':
        self.over(self.players_color(player_is_white))
        return ''
      elif start == 'R':
        self.over('Both players')
        return ''
      
      try:
        x = int(start)
        y = int(input('Give y-coordinate of piece you want to move: '))
        piece = board_instance.get_piece_at(x, y)
      except Exception:
        print('That is not a correct input, try again')
        continue
      
      if piece == None:
        print('That is not a piece, try again')
        continue
      elif piece.is_white != player_is_white:
        print('That is not your piece, try again')
        continue
      
      position = [x, y]
      
      possible_moves = piece.possible_moves(board_instance)
      
      if possible_moves == []:
        print('This piece has no moves, pick another piece')
        continue
      print('These are the moves the piece you have chosen can make', possible_moves)
      
      try:
        x_new = int(input('Give x-cordinate you wan to move to: '))
        y_new = int(input('Give y-cordinate you wan to move to: '))
      except Exception:
        print('That is not a correct input, try again')
        continue
      
      new_position = (x_new, y_new)
      
      if new_position in possible_moves:
        board_instance.move(position, new_position)
        break
      else:
        print('That is not a valid position for that piece, try again')
  
  def over(self, winner):
    self.is_done = True
    self.winner = winner

if __name__ == "__main__":
  board_instance = Board()
  game_instance = Game()
  player_is_white = True
  #True is white False is black for player_is_white
  while game_instance.is_done == False:
    game_instance.player_move(player_is_white)
    player_is_white = not player_is_white
  print(f'{game_instance.winner} won')