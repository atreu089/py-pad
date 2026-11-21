# imports
import tkinter as tk
import json 
from tkinter import filedialog 


# window
root = tk.Tk()
root.title("py-pad")

canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack()

# state
current_color = "black"
brush_size = 2
mode = "draw"
last_x, last_y = None, None
strokes = []
text_boxes = []



# functions
def paint(event):
    global last_x, last_y
    if mode == "draw":
        if last_x is not None and last_y is not None:
            canvas.create_line(
                last_x,
                last_y,
                event.x,
                event.y,
                fill=current_color,
                width=brush_size * 2,
                capstyle=tk.ROUND,
                smooth=True,
            )
            strokes.append({
                "x1": last_x,
                "y1": last_y,
                "x2": event.x,
                "y2": event.y,
                "color": current_color,
                "width": brush_size * 2,
            })
        last_x, last_y = event.x, event.y




def reset_last_pos(event):
    global last_x, last_y
    last_x, last_y = None, None


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
    strokes.clear()
    text_boxes.clear()


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
        text_boxes.append({
            "x": event.x,
            "y": event.y,
            "widget": text_box
        })
        text_box.focus()
        mode = "draw"


def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".pypad",
        filetypes=[("Py-Pad Files", "*.pypad"), ("JSON Files", "*.json")],
    )
    if not file_path:
        return

    saved_texts = []
    for item in text_boxes:
        saved_texts.append({
            "x": item["x"],
            "y": item["y"],
            "text": item["widget"].get(),
        })

    data = {"strokes": strokes, "text_boxes": saved_texts}
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def load_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Py-Pad Files", "*.pypad"), ("JSON Files", "*.json")],
    )
    if not file_path:
        return

    with open(file_path, "r") as file:
        data = json.load(file)

    clear_canvas()

    for line in data["strokes"]:
        canvas.create_line(
            line["x1"],
            line["y1"],
            line["x2"],
            line["y2"],
            fill=line["color"],
            width=line["width"],
            capstyle=tk.ROUND,
            smooth=True,
        )
        strokes.append(line)

    for item in data["text_boxes"]:
        text_box = tk.Entry(canvas, font=("Arial", 12), bg="lightyellow")
        text_box.insert(0, item["text"])
        canvas.create_window(item["x"], item["y"], window=text_box)
        text_boxes.append({
            "x": item["x"],
            "y": item["y"],
            "widget": text_box,
        })


# bindings
canvas.bind("<B1-Motion>", paint)
canvas.bind("<B3-Motion>", erase)
canvas.bind("<Button-1>", add_text)
canvas.bind("<ButtonRelease-1>", reset_last_pos)

# actions
clear_btn = tk.Button(root, text="Clear", command=clear_canvas)
clear_btn.pack(side="left")

# colors
red_btn = tk.Button(root, text="Red", bg="red", fg="white", command=lambda: set_color("red"))
red_btn.pack(side="left")
blue_btn = tk.Button(root, text="Blue", bg="blue", fg="white", command=lambda: set_color("blue"))
blue_btn.pack(side="left")
black_btn = tk.Button(root, text="Black", bg="black", fg="white", command=lambda: set_color("black"))
black_btn.pack(side="left")

# ui
small_btn = tk.Button(root, text="Small", command=lambda: set_size(2))
small_btn.pack(side="left")
medium_btn = tk.Button(root, text="Medium", command=lambda: set_size(5))
medium_btn.pack(side="left")
large_btn = tk.Button(root, text="Large", command=lambda: set_size(10))
large_btn.pack(side="left")
text_btn = tk.Button(root, text="Add Text", command=enable_text_mode)
text_btn.pack(side="left")
save_btn = tk.Button(root, text="Save", command=save_file)
save_btn.pack(side="left")
load_btn = tk.Button(root, text="Load", command=load_file)
load_btn.pack(side="left")

root.mainloop()