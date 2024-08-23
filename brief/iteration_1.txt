# Goal

The primary focus of this iteration is to establish a foundational chess engine capable of generating legal moves and playing a complete game from start to finish, regardless of the quality of those moves. The engine must also implement a basic UCI interface to communicate with a GUI or other chess programs.

# Key Goals

* Move Generation: The engine should be able to generate all legal moves for any given position on the chessboard.

* Game Play: The engine should be capable of playing a full game of chess, making legal moves in response to its opponent's moves until a checkmate, stalemate, or draw occurs.

* UCI Interface: The engine must implement a basic UCI interface, capable of:

  Receiving and understanding essential UCI commands like ucinewgame, position, go, etc.
  Responding with its chosen move using the bestmove command.
  Potentially sending basic information like evaluation scores using the info command.

# Non-Goals

* Strength: At this stage, the engine's playing strength is not a priority. The focus is on functionality and UCI compatibility.

* Advanced UCI Features: Complex UCI features like time management, opening books, or endgame tablebases are not required in this iteration.

# Success Criteria

* The engine can successfully play a complete game of chess against a human or another engine via a UCI-compliant interface.
* All moves made by the engine are legal according to the rules of chess.
* The engine responds correctly to basic UCI commands and provides its chosen move in the expected format.

# Note

This first iteration is focused on establishing a functional foundation for further development. Subsequent iterations will focus on improving the engine's playing strength, optimizing its performance, and implementing more advanced UCI features.
