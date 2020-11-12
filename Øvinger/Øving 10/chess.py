class Piece:
    def __init__(self, side, type, position_x, position_y):
        self.is_white = side.lower() == 'white'
        self.is_alive = True
        self.type = type
        self.y = position_y
        self.x = position_x
    
    def is_opposite_piece_at(self, x, y):
        piece = board_instance.get_piece_at(x, y)
        if piece != None:
            return piece.is_white != self.is_white
        else:
            return False

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
            
            if dir_y == 'y':
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
            
            if dir_y == 'y':
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
        return possible_moves

class King(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.x
        y = self.y
        return possible_moves

class Board:
    def __init__(self):
        self.board=[[Rook('white', Rook, 1, 1), Knight('white', Knight, 2, 1), Bishop('white', Bishop, 3, 1), Queen('white', Queen, 4, 1), King('white', King, 5, 1), Bishop('white', Bishop, 6, 1), Knight('white', Knight, 7, 1), Rook('white', Rook, 8, 1)],
                    [Pawn('white', Pawn, 1, 2), Pawn('white', Pawn, 2, 2), Pawn('white', Pawn, 3, 2), Pawn('white', Pawn, 4, 2), Pawn('white', Pawn, 5, 2), Pawn('white', Pawn, 6, 2), Pawn('white', Pawn, 7, 2), Pawn('white', Pawn, 8, 2)], 
                    [None, None, None, None, None, None, None, None], 
                    [None, None, None, None, None, None, None, None], 
                    [None, None, None, None, None, None, None, None], 
                    [None, None, None, None, None, None, None, None], 
                    [Pawn('black', Pawn, 1, 7), Pawn('black', Pawn, 2, 7), Pawn('black', Pawn, 3, 7), Pawn('black', Pawn, 4, 7), Pawn('black', Pawn, 5, 7), Pawn('black', Pawn, 6, 7), Pawn('black', Pawn, 7, 7), Pawn('black', Pawn, 8, 7)], 
                    [Rook('black', Rook, 1, 8), Knight('black', Knight, 2, 8), Bishop('black', Bishop, 3, 8), Queen('black', Queen, 4, 8), King('black', King, 5, 8), Bishop('black', Bishop, 6, 8), Knight('black', Knight, 7, 8), Rook('black', Rook, 8, 8)]]    
    
    def draw(self):
        pass
    
    def get_piece_at(self, x, y):
        return self.board[y-1][x-1]
    
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
    def player_tunrn(self, player_to_move):
        pass
    def is_in_check(self, player_to_move):
        pass
    def over(self, player_to_move, score):
        self.is_done = True

#for å være i sjakk, sjekker om spilleren er i sjakk, hvis den ar det printes 'You are in check form (piece symbol)
#at (x, y)'
if __name__ == "__main__":
    board_instance = Board()
    game_inatance = Game()
    players_turn = True
    #True is white False is black for players_turn
    while game_inatance.is_done == False:
        game_inatance.player_turn(players_turn)
        players_turn = not players_turn
    print(f'{game_inatance.winner} is the Winner')
    
