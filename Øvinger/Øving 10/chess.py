class Piece:
    def __init__(self, side, position_x, position_y):
        self.is_white = side.lower() == 'white'
        self.is_alive = True
        self.y = position_y
        self.x = position_x
    
    def is_opposite_piece_at(self, x, y):
        piece = board_instance.get_piece_at(x, y)
        if piece != None:
            return piece.is_white != self.is_white
        else:
            return False
    
    def __str__(self):
        return str(type(self))[17: -2]

class Pawn(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        
        def is_in_start_position():
            if self.is_white:
                return self.y == 2
            else:
                return self.y == 7
        
        def direction_lenght(num_1, num_2):
            if self.is_white:
                return num_1 + num_2
            else:
                return num_1 - num_2
        
        if board_instance.get_piece_at(x, direction_lenght(y, 1)) == None:
            possible_moves.append((x, direction_lenght(y, 1)))
            
            if is_in_start_position() and board_instance.get_piece_at(x, direction_lenght(y, 2)) == None:
                possible_moves.append((x, direction_lenght(y, 2)))
        
        if self.is_opposite_piece_at(x + 1, direction_lenght(y, 1)):
            possible_moves.append((x + 1, direction_lenght(y, 1)))
        
        if self.is_opposite_piece_at(x - 1, direction_lenght(y, 1)):
            possible_moves.append((x - 1, direction_lenght(y, 1)))
        return possible_moves

class Rook(Piece):
    def possible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        
        def search_staight(i, maintained_side):
            if maintained_side == 'y':
                search = i, y
            elif maintained_side == 'x':
                search = x, i
            
            search_piece = board_instance.get_piece_at(*search)
            if search_piece == None:
                possible_moves.append(search)
                return False
            elif self.is_opposite_piece_at(*search):
                possible_moves.append(search)
                return True
            else:
                return True
        
        for i in reversed(range(1, x)):
            if search_staight(i, 'y'):
                break        
        for i in range(x + 1, 8 - x + 1):
            if search_staight(i, 'y'):
                break        
        for i in range(1, y):
            if search_staight(i, 'x'):
                break
        for i in reversed(range(y + 1, 8 - y + 1)):
            if search_staight(i, 'x'):
                break
        return possible_moves

class Bishop(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        
        def distance_to_edge(dir_x, dir_y):
            if dir_x == '+':
                disance_to_edge_x = 9 - x
            elif dir_x == '-':
                disance_to_edge_x = x
            
            if dir_y == '+':
                disance_to_edge_y = 9 - y            
            elif dir_y == '-':
                disance_to_edge_y = y
            
            if disance_to_edge_x > disance_to_edge_y:
                return disance_to_edge_y
            
            elif disance_to_edge_x < disance_to_edge_y:
                return disance_to_edge_x
            
        def search(i, dir_x, dir_y):
            if dir_x == '+':
                new_x = x + i
            elif dir_x == '-':
                new_x = x - i
            
            if dir_y == '+':
                new_y = y + i
            elif dir_y == '-':
                new_y = x - i
            return new_x, new_y
        
        def diagonal_search(dir_x, dir_y):
            for i in range(1, distance_to_edge(dir_x, dir_y)):
                search_spot = search(i, dir_x, dir_y)
                search_piece = board_instance.get_piece_at(*search_spot)
                if search_piece == None:
                    possible_moves.append(search_spot)
                elif self.is_opposite_piece_at(*search_spot):
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
    def posible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        
        def distance_to_edge(dir_x, dir_y):
            if dir_x == '+':
                disance_to_edge_x = 9 - x
            elif dir_x == '-':
                disance_to_edge_x = x
            
            if dir_y == '+':
                disance_to_edge_y = 9 - y            
            elif dir_y == '-':
                disance_to_edge_y = y
            
            if disance_to_edge_x > disance_to_edge_y:
                return disance_to_edge_y
            
            elif disance_to_edge_x < disance_to_edge_y:
                return disance_to_edge_x
            
        def search(i, dir_x, dir_y):
            if dir_x == '+':
                new_x = x + i
            elif dir_x == '-':
                new_x = x - i
            
            if dir_y == '+':
                new_y = y + i
            elif dir_y == '-':
                new_y = x - i
            return new_x, new_y
        
        def diagonal_search(dir_x, dir_y):
            for i in range(1, distance_to_edge(dir_x, dir_y)):
                search_spot = search(i, dir_x, dir_y)
                search_piece = board_instance.get_piece_at(*search_spot)
                if search_piece == None:
                    possible_moves.append(search_spot)
                elif self.is_opposite_piece_at(*search_spot):
                    possible_moves.append(search_spot)
                    break
                else:
                    break
        
        diagonal_search('+', '+')
        diagonal_search('+', '-')
        diagonal_search('-', '+')
        diagonal_search('-', '-')
        
        def search_staight(i, maintained_side):
            if maintained_side == 'y':
                search = i, y
            elif maintained_side == 'x':
                search = x, i
            
            search_piece = board_instance.get_piece_at(*search)
            if search_piece == None:
                possible_moves.append(search)
                return False
            elif self.is_opposite_piece_at(*search):
                possible_moves.append(search)
                return True
            else:
                return True
        
        for i in reversed(range(1, x)):
            if search_staight(i, 'y'):
                break        
        for i in range(x + 1, 8 - x + 1):
            if search_staight(i, 'y'):
                break        
        for i in range(1, y):
            if search_staight(i, 'x'):
                break
        for i in reversed(range(y + 1, 8 - y + 1)):
            if search_staight(i, 'x'):
                break
        return possible_moves

class Knight(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        
        def knight_search(start_x, start_y):
            move_types = [(-2, -1), (-2, +1), (+2, -1), (+2, +1), (-1, -2), (-1, +2), (+1, -2), (+1, +2)]
            possible_positions = []
            for (x, y) in move_types:
                x_possible = start_x + x
                y_possible = start_y + y
                if 0 < x_possible <= 8 and 0 < y_possible <= 8:
                    possible_positions.append([x_possible, y_possible])
            return possible_positions
        searchable_spot = knight_search(x, y)
        
        for search in searchable_spot:
            search_piece = board_instance.get_piece_at(*search)
            if search_piece == None or self.is_opposite_piece_at(*search):
                possible_moves.append(search)
        return possible_moves

class King(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        
        def king_search(start_x, start_y):
            move_types = [(-1, -1), (-1, 0), (-1, +1), (0, +1), (0, -1), (+1, +1), (+1, 0), (+1, -1)]
            possible_positions = []
            for (x, y) in move_types:
                x_possible = start_x + x
                y_possible = start_y + y
                if 0 < x_possible <= 8 and 0 < y_possible <= 8:
                    possible_positions.append([x_possible, y_possible])
            return possible_positions
        searchable_spot = king_search(x, y)
        
        for search in searchable_spot:
            search_piece = board_instance.get_piece_at(*search)
            if search_piece == None or self.is_opposite_piece_at(*search):
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
    
    def get_piece_at(self, x, y):
        return self.board[y-1][x-1]
    
    def draw(self):
        piece_symbols = {'Pawn': ['♙', '♟'], 'Rook': ['♖', '♜'], 'Bishop': ['♗', '♝'], 'Knight': ['♘', '♞'], 'Queen': ['♕', '♛'], 'King': ['♔', '♚']}
        def symbol_at(x, y):
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
    
    def move(self, start, end):
        piece = self.get_piece_at(*start)
        oposing_piece = self.get_piece_at(*end)
        
        if piece != None or piece.is_white == oposing_piece.is_white:
            raise ValueError
        #TODO Husk try exept for function
        if oposing_piece != None:
            oposing_piece.is_alive = False
            oposing_piece.x = None
            oposing_piece.y = None
        
        piece.x = end[0]
        piece.y = end[1]
        self.board[start[1]-1][start[0]-1] = None
        self.board[end[1]-1][end[0]-1] = piece

class Game:    
    def __init__(self):
        self.is_done = False
        self.winner = None    
    def player_move(self, player_to_move):
        pass
    def is_in_check(self, player_to_move):
        pass
    def over(self, player_to_move, score):
        self.is_done = True

# for å være i sjakk, sjekker om spilleren er i sjakk, hvis den ar det printes 'You are in check form (piece symbol)
# at (x, y)'
if __name__ == "__main__":
    board_instance = Board()
    game_inatance = Game()
    players_turn = True
    #True is white False is black for players_turn
    while game_inatance.is_done == False:
        game_inatance.player_move(players_turn)
        players_turn = not players_turn
    print(f'{game_inatance.winner} is the Winner')
