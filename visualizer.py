def print_cube(cube):
    f = cube.faces
    def format_face(face):
        return [" ".join(row) for row in f[face]]

    U, D, L, R, F, B = map(format_face, ['U', 'D', 'L', 'R', 'F', 'B'])

    print("      " + U[0])
    print("      " + U[1])
    print("      " + U[2])
    for i in range(3):
        print(f"{L[i]}   {F[i]}   {R[i]}   {B[i]}")
    print("      " + D[0])
    print("      " + D[1])
    print("      " + D[2])
