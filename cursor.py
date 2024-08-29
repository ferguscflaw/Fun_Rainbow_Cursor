import tkinter as tk
import sys
import os

try:
    waiting = int(sys.argv[1])
except:
    timetowait = input("No waiting time. Continue with default? Answer y or n.\n> ")
    if timetowait == "y":
        waiting = 750
    else:
        waiting = int(input("Waiting Time\n> "))

os.system("cls")
os.system("title Cursor_Program_Running")

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', 1)
root.attributes('-alpha', 0.6)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
iteration = 0
screenstrength = 0.6

canvas = tk.Canvas(root, width=screen_width, height=screen_height)
canvas.pack(fill='both', expand=True)
canvas.config(bg='#000000')

def exitscreen():
    root.destroy()

def draw_rainbow_trail(event):
    global iteration, waiting
    x, y = event.x, event.y
    colors = ['#FF0000', '#FF7F00', '#FFFF00', '#7FFF00', '#00FF00', '#00FF7F', '#00FFFF', '#007FFF', '#0000FF', '#7F00FF', '#FF00FF', '#FF007F']
    size = 20
    dot = canvas.create_oval(x - size, y - size, x + size, y + size, outline='', fill=colors[iteration])
    iteration = (iteration + 1) % len(colors)
    root.after(waiting, lambda: canvas.delete(dot))

def strength():
    global screenstrength
    newstrength = (screenstrength + 0.1) % 1
    if newstrength == 0:
        newstrength = 0.1
    root.attributes('-alpha', newstrength)
    screenstrength = newstrength

canvas.bind("<Button-3>", lambda event: root.destroy())
canvas.bind('<Motion>', draw_rainbow_trail)
root.bind('<Tab>', lambda event: strength())
root.mainloop()