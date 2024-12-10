import simplegui

# Canvas 
frame_width = int(input("Initial Width? "))
frame_height = int(input("Initial Height? "))

# Face false statements
show_arafath = False
show_fahim = False
show_aarya = False
show_amelia = False

# Draw handler
def draw(canvas):
    if show_arafath:
        draw_arafath(canvas)
    if show_fahim:
        draw_fahim(canvas)
    if show_aarya:
        draw_aarya(canvas)
    if show_amelia:
        draw_amelia(canvas)
    if show_arafath and show_fahim and show_aarya and show_amelia:
        draw_all_faces(canvas)

# Draw individual faces
#draws arafaths face
def draw_arafath(canvas):  # Happy face
    cx, cy = frame_width / 4, frame_height / 4
    radius = min(frame_width, frame_height) / 6
    canvas.draw_circle((cx, cy), radius, 10, "#FCF4A3", "#FCF4A3")  # Face
    canvas.draw_circle((cx - radius / 2, cy - radius / 3), radius / 8, 2, "Black", "White")  # Left Eye
    canvas.draw_circle((cx + radius / 2, cy - radius / 3), radius / 8, 2, "Black", "White")  # Right Eye
    canvas.draw_arc((cx, cy), radius / 2, 0, 3.14, 3, "Black")  # mouth
#draws fahims face
def draw_fahim(canvas):  # Sad face
    cx, cy = 3 * frame_width / 4, frame_height / 4
    radius = min(frame_width, frame_height) / 6
    canvas.draw_circle((cx, cy), radius, 10, "Yellow", "Yellow")  # head
    canvas.draw_circle((cx - radius / 3, cy - radius / 3), radius / 10, 2, "Black", "White")  # Left Eye
    canvas.draw_circle((cx + radius / 3, cy - radius / 3), radius / 10, 2, "Black", "White")  # Right Eye
    canvas.draw_arc((cx, cy + radius / 4), radius / 2, 3.14, 2 * 3.14, 3, "Black")  # mouth
#draws aaryas face
def draw_aarya(canvas):  # Surprised face
    cx, cy = frame_width / 4, 3 * frame_height / 4
    radius = min(frame_width, frame_height) / 6
    canvas.draw_circle((cx, cy), radius, 10, "Yellow", "Yellow")  # face
    canvas.draw_circle((cx - radius / 3, cy - radius / 3), radius / 6, 2, "Black", "White")  # Left Eye
    canvas.draw_circle((cx + radius / 3, cy - radius / 3), radius / 6, 2, "Black", "White")  # Right Eye
    canvas.draw_circle((cx, cy + radius / 3), radius / 4, 3, "Black", "White")  # mouth
#draws amelias face
def draw_amelia(canvas):  # Angry face
    cx, cy = 3 * frame_width / 4, 3 * frame_height / 4
    radius = min(frame_width, frame_height) / 6
    canvas.draw_circle((cx, cy), radius, 10, "#a88297", "#a88297")  # Face
    canvas.draw_circle((cx - radius / 3, cy - radius / 3), radius / 6, 10, "Black", "White")  # left eye
    canvas.draw_circle((cx + radius / 3, cy - radius / 3), radius / 6, 10, "Black", "White")  # right Eye
    canvas.draw_line((cx - radius / 2, cy - radius / 2), (cx - radius / 4, cy - radius / 3), 3, "Black")  # eyebrow
    canvas.draw_line((cx + radius / 2, cy - radius / 2), (cx + radius / 4, cy - radius / 3), 3, "Black")  # Eyebrow
    canvas.draw_line((cx - radius / 3, cy + radius / 4), (cx + radius / 3, cy + radius / 4), 5, "Black")  # mouth
#gives ability to draw
def draw_all_faces(canvas):
    draw_arafath(canvas)
    draw_fahim(canvas)
    draw_aarya(canvas)
    draw_amelia(canvas)

# Button 
#Shows arafaths button
def toggle_arafath():
    global show_arafath, show_fahim, show_aarya, show_amelia
    reset_faces()
    show_arafath = not show_arafath
# Shows fahims button
def toggle_fahim():
    global show_arafath, show_fahim, show_aarya, show_amelia
    reset_faces()
    show_fahim = not show_fahim
#Shows aaryas button
def toggle_aarya():
    global show_arafath, show_fahim, show_aarya, show_amelia
    reset_faces()
    show_aarya = not show_aarya
#Shows amelias button
def toggle_amelia():
    global show_arafath, show_fahim, show_aarya, show_amelia
    reset_faces()
    show_amelia = not show_amelia
#Shows "all" button
def toggle_all():
    global show_arafath, show_fahim, show_aarya, show_amelia
    reset_faces()
    show_arafath = show_fahim = show_aarya = show_amelia = True
#Clears all faces
def reset_faces():
    global show_arafath, show_fahim, show_aarya, show_amelia
    show_arafath = show_fahim = show_aarya = show_amelia = False

# Create the frame
frame = simplegui.create_frame("Faces Toggle", frame_width, frame_height)
frame.set_canvas_background("Silver")
frame.set_draw_handler(draw)

# Add buttons
frame.add_button("Arafath", toggle_arafath, 150)
frame.add_button("Fahim", toggle_fahim, 150)
frame.add_button("Aarya", toggle_aarya, 150)
frame.add_button("Amelia", toggle_amelia, 150)
frame.add_button("All Faces", toggle_all, 150)

# Start the frame
frame.start()


