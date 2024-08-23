import unittest
from engine import ChessEngine

class TestChessEngine(unittest.TestCase):

    def setUp(self):
        self.engine = ChessEngine()

    def test_uci_initialization(self):
        self.engine.handle_uci_command('uci')
        self.assertEqual(self.engine.responses[-1], 'uciok')

    def test_isready_command(self):
        self.engine.handle_uci_command('isready')
        self.assertEqual(self.engine.responses[-1], 'readyok')

    def test_ucinewgame_command(self):
        self.engine.handle_uci_command('ucinewgame')
        self.assertEqual(self.engine.board, self.engine.create_initial_board())
        self.assertEqual(self.engine.current_turn, 'w')
        self.assertEqual(self.engine.move_history, [])

    def test_position_command(self):
        self.engine.handle_uci_command('position startpos')
        self.assertEqual(self.engine.board, self.engine.create_initial_board())

    def test_go_command(self):
        self.engine.handle_uci_command('go')
        self.assertNotEqual(self.engine.responses[-1], 'bestmove e2e4')

    def test_move_generation(self):
        moves = self.engine.generate_legal_moves()
        self.assertIsInstance(moves, list)

    def test_make_move(self):
        move = 'e2e4'
        self.assertTrue(self.engine.make_move(move))
        self.assertEqual(self.engine.move_history[-1], move)
        self.assertEqual(self.engine.current_turn, 'b')

    def test_castling(self):
        self.engine.board = [
            ['r', '.', '.', '.', 'k', '.', '.', 'r'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['R', '.', '.', '.', 'K', '.', '.', 'R']
        ]
        self.engine.current_turn = 'w'
        self.assertTrue(self.engine.make_move('e1g1'))  # White kingside castling
        self.assertEqual(self.engine.board[7][4], '.')
        self.assertEqual(self.engine.board[7][6], 'K')
        self.assertEqual(self.engine.board[7][7], '.')
        self.assertEqual(self.engine.board[7][5], 'R')

    def test_en_passant(self):
        self.engine.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', '.', 'p', 'p', 'p'],
            ['.', '.', '.', '.', 'p', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', '.', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.engine.current_turn = 'w'
        self.assertTrue(self.engine.make_move('e5d6'))  # White en passant capture
        self.assertEqual(self.engine.board[4][4], '.')
        self.assertEqual(self.engine.board[5][3], 'P')

    def test_pawn_promotion(self):
        self.engine.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', '.', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.engine.current_turn = 'w'
        self.assertTrue(self.engine.make_move('e7e8'))
        self.assertEqual(self.engine.board[0][4], 'Q')

    def test_move_validation(self):
        self.engine.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.engine.current_turn = 'w'
        self.assertTrue(self.engine.is_valid_move('e2e4'))
        self.assertFalse(self.engine.is_valid_move('e2e5'))

    def test_full_uci_protocol(self):
        self.engine.handle_uci_command('uci')
        self.assertEqual(self.engine.responses[-1], 'uciok')
        self.engine.handle_uci_command('isready')
        self.assertEqual(self.engine.responses[-1], 'readyok')
        self.engine.handle_uci_command('ucinewgame')
        self.assertEqual(self.engine.board, self.engine.create_initial_board())
        self.engine.handle_uci_command('position startpos')
        self.assertEqual(self.engine.board, self.engine.create_initial_board())
        self.engine.handle_uci_command('go')
        self.assertNotEqual(self.engine.responses[-1], 'bestmove e2e4')

if __name__ == '__main__':
    unittest.main()
