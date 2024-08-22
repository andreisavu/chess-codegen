import chess

def test_chess_opening_move():
    board = chess.Board()
    board.push_san("e4")
    assert board.san(board.peek()) == "e4"
