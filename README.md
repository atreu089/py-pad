# Py-Pad

Py-Pad is a small hybrid notepad built with Python and Tkinter. It combines freehand drawing with on-canvas text in a simple, single-window interface.

> **Status:** Work in progress, version 0.2

## Features

- Draw on a 600 x 400 white canvas.
- Add text boxes directly onto the canvas.
- Choose red, blue, or black ink.
- Use small, medium, or large brush sizes.
- Erase strokes by holding the right mouse button and moving.
- Clear all drawings and text at once.
- Save and reopen drawings and text as `.pypad` or `.json` files.

## Requirements

- Python 3
- Tkinter

Tkinter is included with most standard Python installations. No third-party packages are required.

## Getting started

Clone or download this repository, then run the app from its directory:

```bash
python main.py
```

## Using Py-Pad

1. Drag the left mouse button across the canvas to draw.
2. Select **Red**, **Blue**, or **Black** to change the ink color.
3. Select **Small**, **Medium**, or **Large** to change the brush size.
4. Select **Add Text**, then click the canvas where the text box should appear.
5. Drag the right mouse button across the canvas to erase.
6. Select **Clear** to remove everything from the canvas.
7. Select **Save** or **Load** to store or reopen a file.

Saved files contain the canvas strokes and text box positions in JSON format.

## Roadmap

- Dedicated text notes view
- Task checklists
- Additional drawing tools and interface improvements
