import tkinter as tk
from .state import Car
from tkinter import ttk
from PIL import Image,ImageTk


# init state
state = new Car

BACKGROUND_COLOUR = "white"
win = tk.Tk()
win.configure(bg=BACKGROUND_COLOUR)
win.title("Express Assess")
win.geometry("720x1280")

tabcontrol = ttk.Notebook(win)

front_tab = ttk.Frame(tabcontrol)
rear_tab = ttk.Frame(tabcontrol)
left_tab = ttk.Frame(tabcontrol)
right_tab = ttk.Frame(tabcontrol)
tabcontrol.add(front_tab, text="front_tab")
tabcontrol.add(rear_tab, text="rear_tab")
tabcontrol.add(left_tab, text="left_tab")
tabcontrol.add(right_tab, text="right_tab")
tabcontrol.pack(expand=1, fill="both")

# front
# lights
# bumper
# bonnet
# windscreen
# what other parts??


# rear
# lights
# what other parts go here??


# left
# doors
# windows
# what others??

# right
# doors
# windows
# what others??

img = Image.open("./assets/part.png")
img = img.resize((300,300))
image = ImageTk.PhotoImage(img)
la = tk.Label(front_tab, image=image)
la.pack()
win.mainloop()


