import tkinter as tk
import time


root = tk.Tk()
root.title("Paint")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

current_color = "black"
brush_size = 2


def paint(event):
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


canvas.bind("<B1-Motion>", paint)
canvas.bind("<B3-Motion>", erase)

# COLORS


clear_btn = tk.Button(root, text="Clear", command=clear_canvas)
clear_btn.pack(side="left")
red_btn = tk.Button(root, text="Red", bg="red", fg="white", command=lambda: set_color("red"))
red_btn.pack(side="left")
blue_btn = tk.Button(root, text="Blue", bg="blue", fg="white", command=lambda: set_color("blue"))
blue_btn.pack(side="left")
black_btn = tk.Button(root, text="Black", bg="black", fg="white", command=lambda: set_color("black"))
black_btn.pack(side="left")

# BRUSH SIZES
small_btn = tk.Button(root, text="Small", command=lambda: set_size(2))
small_btn.pack(side="left")
medium_btn = tk.Button(root, text="Medium", command=lambda: set_size(5))
medium_btn.pack(side="left")
large_btn = tk.Button(root, text="Large", command=lambda: set_size(10))
large_btn.pack(side="left")

# Special Clock Feature Cause I was bored and wanted to add a clock to the app

clock = tk.Label(root, bg="white")
clock.place(relx=1.0, rely=0.0, anchor="ne")


def tick():
    clock.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, tick)


tick()
root.mainloop()
