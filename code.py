#CFU 17
#name
#12/6/24
#Period 5-6
#sample code for scaling images
import simplegui
frame_width = int(input("Initial Width? ")) 
frame_height = int(input("Initial Height? ")) 

#Shape visibility  toggles
show_square = True
show_circle = True
show_triangle = True
show_ecllipse = True

shape1 = shape2 = False

frame = None # Global ref to frame

def all_shapes():
    global shape1, shape2
    shape1 = shape2 = False
    
def toggle_triangle():
    global show_triangle
    show_triangle = not show_triangle
      
    
def draw_triangle(canvas, cx, cy, size):
    #draw the shape
    half_size = size/2
    canvas.draw_polygon([(cx,cy - half_size), 
                         (cx - half_size, cy + half_size),
                         (cx+half_size, cy + half_size)], 2, "Blue", "Blue")
frame = None # Global ref
def draw(canvas):
    quadrant_width = frame_width/2
    quadrant_height = frame_height/2
    if show_triangle:
        draw_triangle(canvas, quadrant_width/2, frame_height - quadrant_height/2, 100) # Triangle in bottom left



def create_frame():
    global frame
    frame = simplegui.create_frame("CFU 17", frame_width, frame_height)
    frame.set_canvas_background("silver")
    frame.add_button("triangle", toggle_triangle, 150)
    frame.set_draw_handler(draw)
    frame.start()

create_frame()
