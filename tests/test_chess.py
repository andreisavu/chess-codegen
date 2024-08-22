import chess

def test_chess_opening_move():
    board = chess.Board()
    board.push(chess.Move.from_uci("e2e4"))
    assert board.peek() == chess.Move.from_uci("e2e4")
