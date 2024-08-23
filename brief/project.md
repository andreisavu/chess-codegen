# Python Chess Engine from Scratch

## Overall Goal

The overarching objective of this project is to develop a fully functional chess engine implemented entirely using standard Python library functions. This means no external chess libraries or modules will be utilized. The development process will follow an iterative approach, incrementally adding features and improving the engine's capabilities over multiple phases.

## Project Scope

The final chess engine should be capable of the following:

### Core Chess Logic

- Represent the chessboard and its pieces accurately.
- Validate and execute legal moves according to the rules of chess.
- Detect check, checkmate, stalemate, and draw conditions.
- Implement move generation, including castling, en passant, and pawn promotion.

### Gameplay

- Play a complete game of chess against a human opponent or another chess engine.
- Provide an interface (e.g., text-based or potentially graphical) for user interaction.
- Optionally, support different time controls for games.

### Additional Features (Potential)

- Implement basic search algorithms (e.g., minimax with alpha-beta pruning) to improve move selection.
- Incorporate simple evaluation heuristics to assess board positions.
- Potentially add support for UCI (Universal Chess Interface) compatibility to interact with other chess programs.

## Iterative Development Approach

The project will be divided into multiple iterations, each focusing on specific milestones and building upon the previous ones. The initial iterations will concentrate on core functionality, ensuring a solid foundation before adding more complex features. This iterative process allows for flexibility, adaptability, and continuous improvement throughout development.

# Project Deliverables

The project deliverables should be two files: engine.py and engine_tests.py.

- engine.py should implement a UCI compatible interface. It should be able to:
  - receive and interpret UCI commands (e.g., ucinewgame, position, go, etc.) from a GUI or another UCI-compliant program.
  - send appropriate responses and information back via the UCI protocol (e.g., bestmove, info, etc.).
  - handle time controls and other game parameters as communicated through UCI.

- engine_tests.py contains various tests to validate the correctness of the UCI implementation in engine.py.

# Iteration 1

## Goal

The primary focus of this iteration is to establish a foundational chess engine capable of generating legal moves and playing a complete game from start to finish, regardless of the quality of those moves. The engine must also implement a basic UCI interface to communicate with a GUI or other chess programs.

## Key Goals

- Move Generation: The engine should be able to generate all legal moves for any given position on the chessboard.
- Game Play: The engine should be capable of playing a full game of chess, making legal moves in response to its opponent's moves until a checkmate, stalemate, or draw occurs.
- UCI Interface: The engine must implement a basic UCI interface, capable of:
  - Receiving and understanding essential UCI commands like ucinewgame, position, go, etc.
  - Responding with its chosen move using the bestmove command.
  - Potentially sending basic information like evaluation scores using the info command.

## Non-Goals

- Strength: At this stage, the engine's playing strength is not a priority. The focus is on functionality and UCI compatibility.
- Advanced UCI Features: Complex UCI features like time management, opening books, or endgame tablebases are not required in this iteration.

## Success Criteria

- The engine can successfully play a complete game of chess against a human or another engine via a UCI-compliant interface.
- All moves made by the engine are legal according to the rules of chess.
- The engine responds correctly to basic UCI commands and provides its chosen move in the expected format.

## Note

This first iteration is focused on establishing a functional foundation for further development. Subsequent iterations will focus on improving the engine's playing strength, optimizing its performance, and implementing more advanced UCI features.
