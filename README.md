# 2D Rubik's Cube

This project is a simple **2D visual Rubik's Cube simulator** with both CLI and GUI (Tkinter) support. It emphasizes **maximum simplicity** and **minimal external libraries** to help explore and learn core algorithms behind cube manipulation and solving logic.

---

## 🚀 Project Goals

- **Educational focus** — intended as a training ground for understanding:
  - Cube rotation logic
  - Puzzle state representation
  - Step-by-step solving strategies
- Future extension planned:
  - A simple **solver algorithm**
  - A basic **neural network** for solving the cube

---

## 🧱 Features

- Visual interface using **Tkinter**
- Console-based visualizer (`visualizer.py`)
- Full support for face rotations (U, D, L, R, F, B)
- Random **scramble** generator
- **Reset** to solved state
- Clean and color-coded UI

---

## 🐍 Requirements

This project uses only the Python Standard Library.

Tested with:

- **Python 3.8+**

No external dependencies required.

---

## 🧩 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/2d_rubiks_cube.git
   cd 2d_rubiks_cube
   ```

2. Run the GUI:
   ```bash
   python gui.py
   ```

3. Or use the terminal visualizer:
   ```bash
   python -i
   >>> from cube import RubiksCube
   >>> from visualizer import print_cube
   >>> cube = RubiksCube()
   >>> cube.move("R")
   >>> print_cube(cube)
   ```

---

## 📁 Folder Structure

- `cube.py` — Core Rubik's Cube logic and move implementation
- `visualizer.py` — Console-based cube visualizer
- `gui.py` — Tkinter-based visual interface

---

## 🔮 Future Plans

- Add **step-by-step solving algorithm**
- Explore simple **neural network** training for cube solutions
- Expand GUI with move history, undo, and scramble logging
