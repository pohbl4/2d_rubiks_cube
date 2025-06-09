import random

class RubiksCube:
    def __init__(self):
        self.reset()

    def reset(self):
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],
            'D': [['Y'] * 3 for _ in range(3)],
            'F': [['G'] * 3 for _ in range(3)],
            'B': [['B'] * 3 for _ in range(3)],
            'L': [['O'] * 3 for _ in range(3)],
            'R': [['R'] * 3 for _ in range(3)],
        }

    def rotate_face_cw(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]

    def rotate_face_ccw(self, face):
        self.faces[face] = [list(row) for row in zip(*self.faces[face])][::-1]

    def move(self, notation):
        valid_moves = {"U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"}
        if notation not in valid_moves:
            print("Unsupported move:", notation)
            return
        method = getattr(self, f'_rotate_{notation[0]}')
        method(prime=notation.endswith("'"))

    def _rotate_U(self, prime):
        self._rotate('U', prime, ['F', 'R', 'B', 'L'], row=0)

    def _rotate_D(self, prime):
        self._rotate('D', not prime, ['F', 'L', 'B', 'R'], row=2)

    def _rotate_L(self, prime):
        self._rotate('L', prime, ['U', 'F', 'D', 'B'], col=0, col_back=True)

    def _rotate_R(self, prime):
        self._rotate('R', not prime, ['U', 'B', 'D', 'F'], col=2, col_back=True)

    def _rotate_F(self, prime):
        self._rotate('F', prime, ['U', 'R', 'D', 'L'], face_map=[
            lambda f: f['U'][2][:],
            lambda f: [row[0] for row in f['R']],
            lambda f: f['D'][0][::-1],
            lambda f: [row[2] for row in f['L']][::-1]
        ], apply_map=[
            lambda f, v: f['U'].__setitem__(2, v),
            lambda f, v: [f['R'][i].__setitem__(0, v[i]) for i in range(3)],
            lambda f, v: f['D'].__setitem__(0, v[::-1]),
            lambda f, v: [f['L'][i].__setitem__(2, v[::-1][i]) for i in range(3)]
        ])

    def _rotate_B(self, prime):
        self._rotate('B', not prime, ['U', 'L', 'D', 'R'], face_map=[
            lambda f: f['U'][0][:],
            lambda f: [row[0] for row in f['L']],
            lambda f: f['D'][2][::-1],
            lambda f: [row[2] for row in f['R']][::-1]
        ], apply_map=[
            lambda f, v: f['U'].__setitem__(0, v),
            lambda f, v: [f['L'][i].__setitem__(0, v[i]) for i in range(3)],
            lambda f, v: f['D'].__setitem__(2, v[::-1]),
            lambda f, v: [f['R'][i].__setitem__(2, v[::-1][i]) for i in range(3)]
        ])

    def _rotate(self, face, prime, adjacent, row=None, col=None, col_back=False, face_map=None, apply_map=None):
        self.rotate_face_ccw(face) if prime else self.rotate_face_cw(face)
        f = self.faces

        if face_map is None:
            if row is not None:
                face_map = [lambda f, adj=adj, r=row: f[adj][r][:] for adj in adjacent]
                apply_map = [lambda f, v, adj=adj, r=row: f[adj].__setitem__(r, v[:]) for adj in adjacent]
            elif col is not None:
                face_map = [lambda f, adj=adj, c=col: [row[c] for row in f[adj]] for adj in adjacent]
                apply_map = [lambda f, v, adj=adj, c=col: [f[adj][i].__setitem__(c, v[i]) for i in range(3)] for adj in adjacent]

        vals = [getter(f) for getter in face_map]
        vals = vals[1:] + [vals[0]] if prime else [vals[-1]] + vals[:-1]

        for setter, val in zip(apply_map, vals):
            setter(f, val)

    def scramble(self, moves=20):
        for _ in range(moves):
            self.move(random.choice(["U", "U'", "D", "D'", "L", "L'", "R", "R'", "F", "F'", "B", "B'"]))
