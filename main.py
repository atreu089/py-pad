import tkinter as tk


root = tk.Tk()
root.title("Paint")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

current_color = "black"
brush_size = 2
mode = "draw"


def paint(event):
    if mode == "draw": 
        canvas.create_oval(
            event.x - brush_size,
            event.y - brush_size,
            event.x + brush_size,
            event.y + brush_size,
            fill=current_color,
            outline=current_color,
        )


def erase(event):
    canvas.create_oval(
        event.x - 10,
        event.y - 10,
        event.x + 10,
        event.y + 2,
        fill="white",
        outline="white",
    )


def clear_canvas():
    canvas.delete("all")


def set_color(new_color):
    global current_color
    current_color = new_color


def set_size(new_size):
    global brush_size
    brush_size = new_size


def enable_text_mode():
    global mode
    mode = "text"


def add_text(event):
    global mode
    if mode == "text":
        text_box = tk.Entry(canvas, font=("Arial", 12), bg="lightyellow")
        canvas.create_window(event.x, event.y, window=text_box)
        text_box.focus()
        mode = "draw"


canvas.bind("<B1-Motion>", paint)
canvas.bind("<B3-Motion>", erase)
canvas.bind("<Button-1>", add_text)

# COLORS
clear_btn = tk.Button(root, text="Clear", command=clear_canvas)
clear_btn.pack(side="left")
red_btn = tk.Button(root, text="Red", bg="red", fg="white", command=lambda: set_color("red"))
red_btn.pack(side="left")
blue_btn = tk.Button(root, text="Blue", bg="blue", fg="white", command=lambda: set_color("blue"))
blue_btn.pack(side="left")
black_btn = tk.Button(root, text="Black", bg="black", fg="white", command=lambda: set_color("black"))
black_btn.pack(side="left")

# BUTTONS
small_btn = tk.Button(root, text="Small", command=lambda: set_size(2))
small_btn.pack(side="left")
medium_btn = tk.Button(root, text="Medium", command=lambda: set_size(5))
medium_btn.pack(side="left")
large_btn = tk.Button(root, text="Large", command=lambda: set_size(10))
large_btn.pack(side="left")
text_btn = tk.Button(root, text="Add Text", command=enable_text_mode)
text_btn.pack(side="left")
root.mainloop()
