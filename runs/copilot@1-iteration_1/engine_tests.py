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
        self.assertEqual(self.engine.responses[-1], 'bestmove e2e4')

    def test_move_generation(self):
        moves = self.engine.generate_legal_moves()
        self.assertIsInstance(moves, list)

    def test_make_move(self):
        move = 'e2e4'
        self.assertTrue(self.engine.make_move(move))
        self.assertEqual(self.engine.move_history[-1], move)
        self.assertEqual(self.engine.current_turn, 'b')

if __name__ == '__main__':
    unittest.main()
