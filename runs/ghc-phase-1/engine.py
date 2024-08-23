import sys

class ChessEngine:
    def __init__(self):
        self.board = self.create_initial_board()
        self.current_turn = 'w'
        self.move_history = []
        self.responses = []

    def create_initial_board(self):
        return [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    def is_valid_move(self, move):
        start_pos = (8 - int(move[1]), ord(move[0]) - ord('a'))
        end_pos = (8 - int(move[3]), ord(move[2]) - ord('a'))
        piece = self.board[start_pos[0]][start_pos[1]]
        target = self.board[end_pos[0]][end_pos[1]]

        if piece == '.':
            return False

        if piece.isupper() and self.current_turn != 'w':
            return False

        if piece.islower() and self.current_turn != 'b':
            return False

        if piece.lower() == 'p':
            if self.current_turn == 'w':
                if start_pos[0] == 6 and end_pos[0] == 4 and start_pos[1] == end_pos[1] and target == '.':
                    return True
                if end_pos[0] == start_pos[0] - 1 and start_pos[1] == end_pos[1] and target == '.':
                    return True
                if end_pos[0] == start_pos[0] - 1 and abs(end_pos[1] - start_pos[1]) == 1 and target.islower():
                    return True
            else:
                if start_pos[0] == 1 and end_pos[0] == 3 and start_pos[1] == end_pos[1] and target == '.':
                    return True
                if end_pos[0] == start_pos[0] + 1 and start_pos[1] == end_pos[1] and target == '.':
                    return True
                if end_pos[0] == start_pos[0] + 1 and abs(end_pos[1] - start_pos[1]) == 1 and target.isupper():
                    return True

        return False

    def make_move(self, move):
        if self.is_valid_move(move):
            self.move_history.append(move)
            start_pos = (8 - int(move[1]), ord(move[0]) - ord('a'))
            end_pos = (8 - int(move[3]), ord(move[2]) - ord('a'))
            piece = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = '.'
            self.board[end_pos[0]][end_pos[1]] = piece

            if piece.lower() == 'p' and (end_pos[0] == 0 or end_pos[0] == 7):
                self.board[end_pos[0]][end_pos[1]] = 'Q' if self.current_turn == 'w' else 'q'

            self.current_turn = 'b' if self.current_turn == 'w' else 'w'
            return True
        return False

    def generate_legal_moves(self):
        moves = []
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if (piece.isupper() and self.current_turn == 'w') or (piece.islower() and self.current_turn == 'b'):
                    for x in range(8):
                        for y in range(8):
                            move = f"{chr(j + ord('a'))}{8 - i}{chr(y + ord('a'))}{8 - x}"
                            if self.is_valid_move(move):
                                moves.append(move)
        return moves

    def handle_uci_command(self, command):
        if command == 'uci':
            self.send_response('id name SimpleChessEngine')
            self.send_response('id author CodeGen')
            self.send_response('uciok')
        elif command == 'isready':
            self.send_response('readyok')
        elif command.startswith('position'):
            self.set_position(command)
        elif command.startswith('go'):
            self.go(command)
        elif command == 'ucinewgame':
            self.new_game()
        elif command == 'quit':
            sys.exit()

    def send_response(self, response):
        print(response)
        self.responses.append(response)

    def set_position(self, command):
        parts = command.split()
        if parts[1] == 'startpos':
            self.board = self.create_initial_board()
        elif parts[1] == 'fen':
            fen = ' '.join(parts[2:])
            self.board = self.fen_to_board(fen)

    def fen_to_board(self, fen):
        board = []
        rows = fen.split('/')
        for row in rows:
            board_row = []
            for char in row:
                if char.isdigit():
                    board_row.extend(['.'] * int(char))
                else:
                    board_row.append(char)
            board.append(board_row)
        return board

    def go(self, command):
        legal_moves = self.generate_legal_moves()
        if legal_moves:
            best_move = legal_moves[0]  # Placeholder for the best move
            self.send_response(f'bestmove {best_move}')

    def new_game(self):
        self.board = self.create_initial_board()
        self.current_turn = 'w'
        self.move_history = []

if __name__ == "__main__":
    engine = ChessEngine()
    while True:
        command = input()
        engine.handle_uci_command(command)
