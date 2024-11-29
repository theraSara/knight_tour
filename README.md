# Knight's Tour Problem (AI for Engineers Course (AIRE305) Project)

This project visualizes the solution to the Knight's Tour Problem, a classic combinatorial problem in chess. It uses Warnsdorff's algorithm to compute the sequence of moves and provides an interactive, graphical representation of the knight's path on a chessboard of customizable size.

## Features
- Interactive graphical interface using **Pygame**.
- Warnsdorff's Algorithm implementation to minimize backtracking.
- Dynamic chessboard size selection.
- Real-time visualization of the knight's path.
- Customizable start position for the knight.

## Prerequisites
- Python 3.7 or later
- Pygame library

## Installation
1. Clone this repository or download the code:
   ```
   git clone https://github.com/theraSara/knight_tour
   cd knights-tour
   ```
2. Install required dependencies:
   ```
   pip install pygame
   ```

## Usage
1. Run the program:
   ```
   python knights_tour.py
   ```
2. Input the following:
   - Chessboard size (min: 5x5, max: 20x20).
   - Starting column and row for the knight.
3. Watch as the knight completes the tour of the chessboard.

## How it works?
- **Algorithm**: Warnsdorff's Algorithm ensures that the knight chooses the next square with the fewest onward moves, reducing the chance of getting stuck.
- **Visualization**:
  - Each visited square is highlighted.
  - Numbers indicate the knight's move sequence.
  - Different colors are used to enhance clarity and aesthetic appeal.

## License
This project is licensed under the MIT License.

