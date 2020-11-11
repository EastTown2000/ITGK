
class Piece:
    def __init__(self, side, type, position_x, position_y):
        self.is_white = side.lower() == 'white'
        self.is_alive = True
        self.type = type
        self.position = (position_x, position_y)
        self.y = position_y
        self.x = position_x
        self.num_moves = 0
    def is_opposite_piece_at(self, x, y):
        piece = board_instance.get_piece_at(x, y)
        if piece != None:
            return piece.is_white != self.is_white
        else:
            return False

class Pawn(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        if self.is_white:
            if board_instance.get_piece_at(x, y + 1) == None:
                possible_moves.append((x, y + 1))
            if self.num_moves == 0 and (x, y + 2) == None and board_instance.get_piece_at(x, y + 1) == None:
                possible_moves.append((x, y + 2))
            if self.is_opposite_piece_at(x + 1, y + 1):
                possible_moves.append((x + 1, y + 1))
            if self.is_opposite_piece_at(x - 1, y + 1):
                possible_moves.append((x - 1, y + 1))
        else:
            if board_instance.get_piece_at(x, y - 1) == None:
                possible_moves.append((x, y - 1))
            if self.num_moves == 0 and (x, y - 2) == None and board_instance.get_piece_at(x, y - 1) == None:
                possible_moves.append((x, y - 2))
            if self.is_opposite_piece_at(x + 1, y - 1):
                possible_moves.append((x + 1, y - 1))
            if self.is_opposite_piece_at(x - 1, y - 1):
                possible_moves.append((x - 1, y - 1))
        return possible_moves

class Rook(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        for i in range(1, x):
            piece = board_instance.get_piece_at(i, y)            
            pass
        for i in range(x + 1, 8 - x + 1):
            pass
        for i in range(1, y):
            pass
        for i in range(y + 1, 8 - y + 1):
            pass
        pass

class Bishop(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        pass

class Knight(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        pass

class Queen(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        pass

class King(Piece):
    def posible_moves(self):
        possible_moves = []
        x = self.position[0]
        y = self.position[1]
        pass

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

class Game:    
    def __init__(self):
        pass
    def game_is_done(self):
        pass
    def player_tunrn(self, player_to_move):
        pass
    def is_in_check(self, player_to_move):
        pass

if __name__ == "__main__":
    board_instance = Board()
    game_inatance = Game()
    players_turn = True
    #True is white False is black for players_turn
    while game_inatance.game_is_done == False:
        game_inatance.player_turn(players_turn)
        players_turn = not players_turn
    print(f'{game_inatance.winner} is the Winner')
    
