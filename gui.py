import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk


# init state

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

window_width = 800
window_height = 500

#place the window on the center of the screen
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

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


