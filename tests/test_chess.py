import chess
from stockfish import Stockfish

def test_chess_opening_move():
    stockfish = Stockfish(path="bin/stockfish")
    board = chess.Board()
    best_move = stockfish.get_best_move()
    board.push(chess.Move.from_uci(best_move))
    assert board.peek() == chess.Move.from_uci(best_move)
