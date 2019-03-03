from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, 'ru')
    commands = file.readlines()
    point_matrix = new_matrix(4,4)
    print("this is transform")
    print (transform)
    print_matrix(transform)

    pass
    for i in range(len(commands)):
        command = commands[i]
        if command == "line\n":
            new_line = commands[i+1].split(" ")
            add_edge(point_matrix, int(new_line[0]), int(new_line[1]), int(new_line[2]), int(new_line[3]), int(new_line[4]), int(new_line[5]))
        elif command == "ident\n":
            ident(transform)
        elif command == "scale\n":
            scale = commands[i+1].split(" ")
            print(scale[0])
            print(scale[1])

            print(scale[2])
            print_matrix(transform)

            matrix_mult(make_scale(float(scale[0]), float(scale[1]), float(scale[2])), transform)
        elif command == "move\n":
            trans = commands[i+1].split(" ")
            matrix_mult(make_translate(float(trans[0]), float(trans[1]), float(trans[2])), transform)
        elif command == "rotate\n":
            rotate = commands[i+1].split(" ")
            if rotate[0] == "x":
                matrix_mult(make_rotX(float(rotate[1])), transform)
            elif rotate[0] == "y":
                matrix_mult(make_rotY(float(rotate[1])), transform)
            else:
                matrix_mult(make_rotZ(float(rotate[1])), transform)
        elif command == "apply\n":
            matrix_mult(transform, point_matrix)
        # elif command == "display\n":
        #     print("JUST DISPLAY")
        #
        #     clear_screen(screen)
        #     for r in range(len(point_matrix)):
        #         for c in range(len(point_matrix[r])):
        #             point_matrix[r][c] = int(point_matrix[r][c])
        #     draw_lines(point_matrix, screen, color)
        #     display(screen)
        elif command == "save\n":
            print("JUST SAVE")

            arr = commands[i + 1].split("\n")
            for r in range(len(point_matrix)):
                for c in range(len(point_matrix[r])):
                    point_matrix[r][c] = int(point_matrix[r][c])
            draw_lines(point_matrix, screen, color)
            save_extension( screen, arr[0])
        elif command == "quit\n":
            print("JUST QUIT")
            break
        else:
            pass
    file.close()
