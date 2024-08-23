# Project Deliverables

The project deliverables should be two files: engine.py and engine_tests.py.

* engine.py should implement a UCI compatible interface. It should be able to:
  - receive and interpret UCI commands (e.g., ucinewgame, position, go, etc.) from a GUI or another UCI-compliant program.
  - send appropriate responses and information back via the UCI protocol (e.g., bestmove, info, etc.).
  - handle time controls and other game parameters as communicated through UCI.

* engine_tests.py contains various tests to validate the correctness of the UCI implementation in engine.py.
