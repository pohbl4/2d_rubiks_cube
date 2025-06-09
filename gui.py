import tkinter as tk
from cube import RubiksCube

COLOR_MAP = {
    'W': 'white',
    'Y': 'yellow',
    'G': 'green',
    'B': 'blue',
    'O': 'orange',
    'R': 'red'
}

class FaceGrid:
    def __init__(self, master, face_id, rotate_callback):
        self.face_id = face_id
        self.rotate_callback = rotate_callback

        self.frame = tk.Frame(master, bd=2, relief='flat')

        # Подфрейм с кнопками
        btn_frame = tk.Frame(self.frame)
        btn_frame.grid(row=0, column=0, columnspan=3)

        rotate_cw = tk.Button(btn_frame, text='↻', width=3, command=lambda: rotate_callback(face_id))
        rotate_ccw = tk.Button(btn_frame, text='↺', width=3, command=lambda: rotate_callback(face_id + "'"))

        rotate_ccw.grid(row=0, column=0, padx=2)
        rotate_cw.grid(row=0, column=1, padx=2)

        # Сетка кубика
        self.grid = [[
            tk.Label(self.frame, width=4, height=2, relief='solid', borderwidth=1)
            for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.grid[i][j].grid(row=i + 1, column=j, padx=1, pady=1)

    def grid_face(self, r, c):
        self.frame.grid(row=r, column=c, padx=10, pady=10)

    def update(self, face_data):
        for i in range(3):
            for j in range(3):
                color = COLOR_MAP.get(face_data[i][j], 'grey')
                self.grid[i][j]['bg'] = color


class CubeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rubik's Cube GUI")
        self.cube = RubiksCube()
        self.history = []

        self.grid_frame = tk.Frame(master)
        self.grid_frame.pack(pady=10)

        self.faces = {}
        positions = {
            'U': (0, 1),
            'L': (1, 0),
            'F': (1, 1),
            'R': (1, 2),
            'B': (1, 3),
            'D': (2, 1),
        }

        for face, (r, c) in positions.items():
            fg = FaceGrid(self.grid_frame, face, self.handle_rotation)
            fg.grid_face(r, c)
            self.faces[face] = fg

        self.update_faces()

        ctrl = tk.Frame(master)
        ctrl.pack(pady=5)
        tk.Button(ctrl, text="Scramble", command=self.scramble).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        tk.Button(ctrl, text="Undo", command=self.undo).pack(side=tk.LEFT, padx=5)

        self.master.bind("<Key>", self.on_key_press)

    def handle_rotation(self, move):
        self.history.append(self.copy_cube_state())
        self.cube.move(move)
        self.update_faces()

    def update_faces(self):
        for face, widget in self.faces.items():
            widget.update(self.cube.faces[face])

    def scramble(self):
        self.history.append(self.copy_cube_state())
        self.cube.scramble()
        self.update_faces()

    def reset(self):
        self.history.clear()
        self.cube = RubiksCube()
        self.update_faces()

    def copy_cube_state(self):
        # Создаем глубокую копию текущего состояния куба для Undo
        return {face: [row[:] for row in grid] for face, grid in self.cube.faces.items()}

    def undo(self):
        if not self.history:
            return
        last_state = self.history.pop()
        self.cube.faces = last_state
        self.update_faces()

    def on_key_press(self, event):
        key = event.char.upper()
        if key in ['U', 'D', 'L', 'R', 'F', 'B']:
            self.handle_rotation(key)
        elif key in ["'", "’"]:  # Обработка апострофа для поворота против часовой
            # Предыдущий ход сделать с апострофом
            if self.history:
                last_move = self.history[-1]
                # Здесь можно доработать для поддержки сложных вводов
                # Пока пропускаем
        # Можно расширить для сложных ходов

if __name__ == "__main__":
    root = tk.Tk()
    app = CubeGUI(root)
    root.mainloop()
