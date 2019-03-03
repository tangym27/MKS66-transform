from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
#
# make_rotX(90)
# make_rotY(90)
# make_rotZ(90)
# make_translate(1,2,3)
# make_scale(1,2,3)
#print_matrix(transform)

parse_file( 'script', edges, transform, screen, color )
print("done")
