import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

# state of car
#
# need make model year parts list
#
class Car:
    make =""
    model=""
    year=0
    undamaged_parts=[]

    def __init__(self, make, model, year, undamaged_parts=[]):
        self.make = make
        self.model = model
        self.year = year
        self.undamaged_parts = undamaged_parts 

    def add_undamaged(self,part_number):
        self.undamaged_parts.append(part_number)

    def remove_undamaged(self,part_number):
        self.undamaged_parts.remove(part_number)

# init state
state= Car("Honda", "Civic", "2009")
print(state.undamaged_parts)
state.add_undamaged("ALSKDJ:LASDKJ")
print(state.undamaged_parts)

BACKGROUND_COLOUR = "white"
win = tk.Tk()
win.configure(bg=BACKGROUND_COLOUR)
win.title("Express Assess")
win.geometry("720x1280")

tabcontrol = ttk.Notebook(win)

home_page = ttk.Frame(tabcontrol)
Q1 = ttk.Frame(tabcontrol)
Q2 = ttk.Frame(tabcontrol)
Q3 = ttk.Frame(tabcontrol)

Result = ttk.Frame(tabcontrol)
tabcontrol.add(home_page, text="Home")
tabcontrol.add(Q1, text="Q1")
tabcontrol.add(Q2, text="Q2")
tabcontrol.add(Q3, text="Q3")

tabcontrol.add(Result, text="Result")
tabcontrol.pack(expand=1, fill="both")

window_width = 800
window_height = 500

#place the window on the center of the screen
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

win.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')



tk.Button(home_page, 
          text='START', 
          bg="indian red", 
          fg="black",
          width = 20,
          height = 2
          ).pack(pady=220,
                 padx=50, 
                 side="top")



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
la = tk.Label(Q1, image=image)
la.pack()
win.mainloop()


