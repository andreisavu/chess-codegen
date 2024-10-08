# UCI Protocol Documentation

## Purpose

The Universal Chess Interface (UCI) protocol defines a communication standard that enables chess engines and graphical user interfaces (GUIs) to interact. It facilitates various aspects of chess gameplay, analysis, and configuration.

## Communication

- The GUI sends commands to the engine via standard input (stdin).
- The engine sends responses to the GUI via standard output (stdout).

## Commands

- **uci**: Initializes the engine and requests identification information.
- **isready**: Confirms that the engine is ready to receive further commands.
- **ucinewgame**: Informs the engine that a new game is starting.
- **position**: Sets up the current board position.
- **go**: Starts the engine's calculation and requests a move.
- **stop**: Stops the engine's calculation.
- **quit**: Terminates the engine.
- Other optional commands and features exist as per the UCI specification.

## Responses

- **id**: Provides identification information (name, author, etc.).
- **uciok**: Confirms that the engine has successfully initialized.
- **readyok**: Confirms that the engine is ready.
- **bestmove**: Communicates the engine's calculated best move.
- **info**: Provides additional information during calculation (e.g., current evaluation, search depth, etc.).

## Data Formats

- Standard Algebraic Notation (SAN) for moves (e.g., "e4", "Nf3", "O-O").
- Forsyth-Edwards Notation (FEN) for board positions.
- Other UCI-specified data formats for various information exchange.

## Example Interaction

GUI: uci
Engine: id name MyChessEngine
Engine: id author John Doe
Engine: uciok

GUI: isready
Engine: readyok

GUI: ucinewgame
GUI: position startpos
GUI: go
Engine: info depth 1 seldepth 1 score cp 214 nodes 45 nps 45000 time 1 pv e2e4
Engine: bestmove e2e4

## Important Notes

- The UCI protocol is constantly evolving; refer to the official documentation for the latest specifications.
- Efficient implementation is crucial for good performance and responsiveness.
- Thorough testing is essential to guarantee compatibility with various GUIs.
