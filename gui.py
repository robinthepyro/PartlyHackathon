import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

def submit():
    print(car.damaged_parts)
    exit()
    # You can later expand this to validate inputs, store data, etc.


class ToggleButton(tb.Button):
    def __init__(self, master, part_name, callback=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.part_name = part_name
        self.status = "ok"
        self.callback = callback
        self.configure(text=part_name, bootstyle=SUCCESS, command=self.toggle)

    def toggle(self):
        # Toggle status
        self.status = "damaged" if self.status == "ok" else "ok"
        style = DANGER if self.status == "damaged" else SUCCESS
        self.configure(bootstyle=style)

        # Call the callback with the updated state
        if self.callback:
            self.callback(self.part_name, self.status)

class Car:
    def __init__(self, make, model, plate, damaged_parts=None):
        self.make = make
        self.model = model
        self.plate = plate
        self.damaged_parts = damaged_parts or []

    def add_damaged(self, part_number):
        self.damaged_parts.append(part_number)

    def remove_damaged(self, part_number):
        self.damaged_parts.remove(part_number)


car = Car("Toyota", "Corolla HB", "JAJ858")

def handle_part_click(part_name, status):
    print(f"Part clicked: {part_name} | Status: {status}")
    if status == "ok":
        if part_name in car.damaged_parts:
            car.damaged_parts.remove(part_name)
    else:
        if part_name not in car.damaged_parts:
            car.damaged_parts.append(part_name)

# --- App window ---
app = tb.Window(themename="darkly")
app.title("Express Assess")
app.geometry("1000x600")

# --- State ---
seconds_elapsed = 0
timer_job = None

# --- Layout: Sidebar + Main ---
sidebar = tb.Frame(app, padding=20)
sidebar.pack(side=LEFT, fill=Y)

main_frame = tb.Frame(app, padding=20)
main_frame.pack(side=LEFT, fill=BOTH, expand=YES)

# --- Sidebar Navigation ---
def switch_tab(tab_name):
    for f in content_frames.values():
        f.pack_forget()
    content_frames[tab_name].pack(fill=BOTH, expand=YES)

ttk_buttons = {
    "Home": lambda: switch_tab("Home"),
    "Front": lambda: switch_tab("Front"),
    "Back": lambda: switch_tab("Back"),
    "Left": lambda: switch_tab("Left"),
    "Right": lambda: switch_tab("Right"),
    "Result": lambda: switch_tab("Result")
}

for label, cmd in ttk_buttons.items():
    tb.Button(sidebar, text=label, command=cmd, bootstyle=SECONDARY).pack(fill=X, pady=5)

# --- Timer logic ---
def update_timer():
    global seconds_elapsed, timer_job
    seconds_elapsed += 1
    timer_label.config(text=f"Timer: {seconds_elapsed}s")
    timer_job = app.after(1000, update_timer)

def start_assessment():
    global seconds_elapsed, timer_job
    seconds_elapsed = 0
    update_timer()
    switch_tab("Front")

# --- Content Frames ---
content_frames = {}

for name in ["Home", "Front", "Back", "Left", "Right", "Result"]:
    content_frames[name] = tb.Frame(main_frame)
    content_frames[name].pack(fill=BOTH, expand=YES)
    content_frames[name].pack_forget()

content_frames["Home"].pack(fill=BOTH, expand=YES)  # default

# --- Timer (shared) ---
timer_label = tb.Label(app, text="Timer: 0s", font=("Segoe UI", 12), bootstyle="danger")
timer_label.place(relx=1.0, rely=0.01, anchor="ne", x=-20)

# --- Home Page ---
tb.Label(content_frames["Home"], text="Express Assess 🚗", font=("Segoe UI", 16)).pack(pady=30)
tb.Button(content_frames["Home"], text="Start Assessment", command=start_assessment, bootstyle=SUCCESS).pack(pady=10)

# --- Car image loader ---
def load_img(path, size=(300, 300)):
    img = Image.open(path).resize(size)
    return ImageTk.PhotoImage(img)

img_front = load_img("./assets/front.png")
img_back = load_img("./assets/back.png")
img_left = load_img("./assets/leftside.png")
img_right = load_img("./assets/rightside.png")

# --- Section builder ---
def build_part_section(frame, image, title, parts):
    image_label = tb.Label(frame, image=image)
    image_label.image = image
    image_label.pack(side=LEFT, padx=20, pady=20)

    parts_frame = tb.LabelFrame(frame, text=f"{title} Parts", padding=10)
    parts_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=10, pady=10)

    for part in parts:
        ToggleButton(parts_frame, part, callback=handle_part_click).pack(pady=5, fill=X)

# --- Tabs ---
build_part_section(
    content_frames["Front"],
    img_front,
    "Front",
    ["Headlights", "Bumper", "Windscreen"]
)

build_part_section(
    content_frames["Back"],
    img_back,
    "Back",
    ["Rear Lights", "Rear Bumper", "Trunk"]
)

build_part_section(
    content_frames["Left"],
    img_left,
    "Left Side",
    ["Left Front Door", "Left Rear Door", "Left Fender"]
)

build_part_section(
    content_frames["Right"],
    img_right,
    "Right Side",
    ["Right Front Door", "Right Rear Door", "Right Fender"]
)

# --- Result Page ---
tb.Label(content_frames["Result"], text="Assessment Complete", font=("Segoe UI", 14)).pack(pady=30)
tb.Button(content_frames["Result"], text="Back to Home", command=lambda: switch_tab("Home"), bootstyle=PRIMARY).pack()


# --- Submit button on all tabs ---
tb.Button(content_frames["Front"], text="Submit", bootstyle=SUCCESS, command=lambda: submit()).pack(side=BOTTOM, pady=10)

tb.Button(content_frames["Back"], text="Submit", bootstyle=SUCCESS, command=lambda: submit()).pack(side=BOTTOM, pady=10)

tb.Button(content_frames["Left"], text="Submit", bootstyle=SUCCESS, command=lambda: submit()).pack(side=BOTTOM, pady=10)

tb.Button(content_frames["Right"], text="Submit", bootstyle=SUCCESS, command=lambda: submit()).pack(side=BOTTOM, pady=10)

tb.Button(content_frames["Result"], text="Submit", bootstyle=SUCCESS, command=lambda: submit()).pack(side=BOTTOM, pady=10)


# --- Run ---
app.mainloop()
