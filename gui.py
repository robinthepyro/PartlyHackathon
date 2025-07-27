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
Q4 = ttk.Frame(tabcontrol)

Result = ttk.Frame(tabcontrol)
tabcontrol.add(home_page, text="Home")
tabcontrol.add(Q1, text="FRONT")
tabcontrol.add(Q2, text="BACK")
tabcontrol.add(Q3, text="LEFT")
tabcontrol.add(Q4, text="RIGHT")



button_start = tk.Button(home_page, text="Start Assessment", command=lambda: tabcontrol.select(print("Assessment Started"), start_assessment()))
button_wind = tk.Button(Q1, text="Windshield", command=lambda: tabcontrol.select(print("Windshield Selected")))
button_headlights = tk.Button(Q2, text="Headlights", command=lambda: tabcontrol.select(print("Headlights Selected")))
button_bumper_front = tk.Button(Q3, text="Front Bumper", command=lambda: tabcontrol.select(print("Front Bumper Selected")))
button_bumper_back = tk.Button(Q4, text="Back Bumper", command=lambda: tabcontrol.select(print))
button_left_front_door = tk.Button(Q1, text="Left Door", command=lambda: tabcontrol.select(print))
button_left_back_door = tk.Button(Q2, text="Left Back Door", command=lambda: tabcontrol.select(print("Left Back Door Selected")))
button_right_front_door = tk.Button(Q3, text="Right Front Door", command=lambda: tabcontrol.select(print("Right Front Door Selected")))
button_right_back_door = tk.Button(Q2, text="Right Door", command=lambda: tabcontrol.select(print("Right back Door Selected")))

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


#timer
timer_label_q1 = tk.Label(Q1, text="Timer: 0s", font=("Arial", 14),fg="red")
timer_label_q1.pack(pady=20)
timer_label_q1.place(relx=1.0, y=10, anchor="ne", x=-10)

timer_label_q2 = tk.Label(Q2, text="Timer: 0s", font=("Arial", 14),fg="red")
timer_label_q2.pack(pady=20)
timer_label_q2.place(relx=1.0, y=10, anchor="ne", x=-10)

timer_label_q3 = tk.Label(Q3, text="Timer: 0s", font=("Arial", 14),fg="red")
timer_label_q3.pack(pady=20)
timer_label_q3.place(relx=1.0, y=10, anchor="ne", x=-10)

timer_label_q4 = tk.Label(Q4, text="Timer: 0s", font=("Arial", 14),fg="red")
timer_label_q4.pack(pady=20)
timer_label_q4.place(relx=1.0, y=10, anchor="ne", x=-10)

timer_label_result = tk.Label(Result, text="Timer: 0s", font=("Arial", 14),fg="red")
timer_label_result.pack(pady=20)
timer_label_result.place(relx=1.0, y=10, anchor="ne", x=-10)

seconds_elapsed = 0

def update_timer():
    global seconds_elapsed, timer_job
    seconds_elapsed += 1
    timer_label_q1.config(text=f"Timer: {seconds_elapsed}s")
    timer_label_q2.config(text=f"Timer: {seconds_elapsed}s")
    timer_label_q3.config(text=f"Timer: {seconds_elapsed}s")
    timer_label_q4.config(text=f"Timer: {seconds_elapsed}s")

    timer_label_result.config(text=f"Timer: {seconds_elapsed}s")


    timer_job = win.after(1000, update_timer)

def start_assessment():
    # Switch to Q1 tab
    tabcontrol.select(Q1)
    # Reset timer and start it
    global seconds_elapsed
    seconds_elapsed = 0
    update_timer()



def on_tab_changed(event):
    global timer_job
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")
    if tab_text == "Result":
        # Cancel the timer updates
        if timer_job is not None:
            win.after_cancel(timer_job)
            timer_job = None

tabcontrol.bind("<<NotebookTabChanged>>", on_tab_changed)
#start button
def go_to_q1():
    tabcontrol.select(Q1)


tk.Button(
    home_page,
    text='START',
    bg="indian red",
    fg="black",
    width=20,
    height=2,
    command=start_assessment
).place(x=300, y=300)

#selection of options
def go_to_q2():
    tabcontrol.select(Q2)

img = Image.open("./assets/part.png")
img = img.resize((200,200))
image = ImageTk.PhotoImage(img)


button_row = tk.Frame(Q1)
button_row.pack(pady=20)

car_parts = [
    {"name": "Hood", "img_path": "./assets/part.png"},
    {"name": "Bumper", "img_path": "./assets/part.png"},
    {"name": "Headlight", "img_path": "./assets/part.png"}
]

images = []

for part in car_parts:
    img = Image.open(part["img_path"]).resize((100, 100))
    photo = ImageTk.PhotoImage(img)
    images.append(photo) 

    # Create the button
    btn = tk.Button(
        button_row,
        image=photo,
        text=part["name"],
        compound="top",
        width=120,
        height=140,
        command=go_to_q2
    )
    btn.pack(side="left", padx=10)



# front
# lights
# bumper
# bonnet
# windscreen
# what other parts??
frontimg = Image.open("./assets/front.png")
backimg = Image.open("./assets/back.png")
leftimg = Image.open("./assets/leftside.png")
rightimg = Image.open("./assets/leftside.png")

frontimg = frontimg.resize((300,300))
backimg = backimg.resize((300,300))
leftimg = leftimg.resize((300,300))
rightimg = rightimg.resize((300,300))
front_image = ImageTk.PhotoImage(frontimg)
back_image = ImageTk.PhotoImage(backimg)
left_image = ImageTk.PhotoImage(leftimg)
right_image = ImageTk.PhotoImage(rightimg)
front_label = tk.Label(Q1, image=front_image)
back_label = tk.Label(Q2, image=back_image)
left_label = tk.Label(Q3, image=left_image)
right_label = tk.Label(Q4, image=right_image)     
front_label.pack()
back_label.pack()
left_label.pack()
right_label.pack()

button_wind.pack(pady=20)
button_headlights.pack(pady=20) 
button_bumper_front.pack(pady=20)
button_bumper_back.pack(pady=20)
button_left_front_door.pack(pady=20)
button_left_back_door.pack(pady=20)
button_right_front_door.pack(pady=20)
button_right_back_door.pack(pady=20)
button_start.pack(pady=20)


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
la = tk.Label(home_page, image=image)
la.pack()
win.mainloop()


