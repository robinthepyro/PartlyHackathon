import json
import ttkbootstrap as tb
import requests
from ttkbootstrap.constants import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import requests
import json
# URL (make sure to add a value for tree_root_ghca_id if needed)
world_tree_url = "https://api.dev3.partly.pro/api/v1/world-tree.search"
vrm_url = "https://api.dev3.partly.pro/api/v1/vrm.search"
vrm_params = {
    "identifier": 
    {
        "plate": "JAJ858",
        "region": "UREG32",
        "state": None
    }
}

vehicle_url = "https://api.dev3.partly.pro/api/v1/vehicles.search"
assembly_url = "https://api.dev3.partly.pro/api/v1/assemblies.v3.search"
# Your Bearer token here
bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5kZXYzLnBhcnRseS5wcm8vIiwic3ViIjoiMzhhMDY5OWYtY2E3Zi00ZDU4LTgzYWUtNDg0YmUzZmViNTM2IiwiaWF0IjoxNzUzNTYwNjI2LCJleHAiOjE3NTM2NjA4MDAsImp0aSI6ImFwaWtleTo1OGNjYzcxMy00MjgzLTQwMDEtYjAyNS0yMzYzMGFjYmJiNjAiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOlt7Imlzc3VlciI6Ii9hcGkvdjEvcmVwYWlyZXJzLnZlcmlmeSIsInBhcmFtZXRlcnMiOnsicmVwYWlyZXJfaWQiOiI5NmEwOGQ2OC05ZjM0LTQ2YmYtYjEwNS1iYzg0M2VkNmJhZjgifSwiZGV0YWlscyI6eyJvcmdhbml6YXRpb25faWQiOiJjOGIzOWUwNS05ODA1LTQ0NTEtOWI1Zi0yOTFmZGZiOTI4NmEiLCJyZXBhaXJlcl9pZCI6Ijk2YTA4ZDY4LTlmMzQtNDZiZi1iMTA1LWJjODQzZWQ2YmFmOCIsInNpdGVfaWRzIjpbXX19LHsiaXNzdWVyIjoiL2FwaS92MS9vcmdhbml6YXRpb25zLnZlcmlmeSIsInBhcmFtZXRlcnMiOnsib3JnYW5pemF0aW9uX2lkIjoiYzhiMzllMDUtOTgwNS00NDUxLTliNWYtMjkxZmRmYjkyODZhIn0sImRldGFpbHMiOnsiaWQiOiJjOGIzOWUwNS05ODA1LTQ0NTEtOWI1Zi0yOTFmZGZiOTI4NmEiLCJwZXJtaXNzaW9ucyI6W3sic2NvcGUiOiJvcmdhbml6YXRpb25fYWRtaW5zIiwiZW50aXR5IjoiYzhiMzllMDUtOTgwNS00NDUxLTliNWYtMjkxZmRmYjkyODZhIn0seyJzY29wZSI6ImJ1c2luZXNzX2FkbWlucyJ9XX19XX0.0v1pBLE1OwN1--8onkvirT_zA1_I15LwChF_Kmq5Qp5xuZATekC31sxbVOHwfQvAbstj-a85j-qUK7N0TOdtww"

# Headers with Authorization
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

vrm_response = requests.post(vrm_url, headers=headers, json={
    "plate": "JAJ858", "region": "UREG32", "state": None})
vrm_chassis = vrm_response.json()["chassis"]
vehicle_params = {
    "identifier": {
        "chassis_number": vrm_chassis # Your VIN 
    },
}

parts = {
    "Windscreen": "GHCA59",
    "Headlights": "GHCA8950",
    "Front Bumper": "GHCA7570",
    "Rear Bumper": "GHCA234",
    "Left Front Door": "GHCA27",
    "Right Front Door": "GHCA416",
    "Left Rear Door": "GHCA468",
    "Right Rear Door": "GHCA520",
    "Right Fender": "GHCA7496",
    "Left Fender": "GHCA7495",
    "Left Rear Light": "GHCA29",
    "Right Rear Light": "GHCA1415"
}

def invert_list(damaged):
    out = list(parts.keys())
    for part in damaged:
        out.remove(part)
    return out

PART_NAMES = ['Headlights', 'Bumper', 'Windscreen', 'Rear Lights', 'Rear Bumper', 'Trunk', 'Left Front Door', 'Left Rear Door', 'Left Fender', 'Right Front Door', 'Right Rear Door', 'Right Fender']


def submit():
    und = invert_list(car.damaged_parts)
    for u in und:
        car.undamaged_parts.append(parts[u])
    complete = populate_children(car.undamaged_parts)

    print("complete = " , complete)
    with open("out.txt","w") as f:
        f.write(", ".join(complete))

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
    def __init__(self, make, model, plate, damaged_parts=None, undamaged_parts=None):
        self.make = make
        self.model = model
        self.plate = plate
        self.damaged_parts = damaged_parts or []
        self.undamaged_parts = undamaged_parts or [] 

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
    ["Left Headlight", "Right Headlight", "Front Bumper", "Windscreen"]
)

build_part_section(
    content_frames["Back"],
    img_back,
    "Back",
    ["Left Rear Light", "Right Rear Light", "Rear Bumper"]
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

def populate_children(part_ids):
    queue = part_ids
    all_children = list(part_ids)
    i = 0
    while queue:
        i += 1
        print(i)
        parent = queue.pop()
        print(parent)
        children = find_part_children(parent)
        all_children.extend(children)
        queue.extend(children)
        if i > 1000:
            break
    return all_children

def find_part_children(part_id):
    world_tree = requests.post(world_tree_url, headers=headers, json={'tree_root_ghca_id': part_id})
    if world_tree.status_code == 200:
        return list(world_tree.json()['nodes'].keys())[1:]
    return []

# --- Run ---
app.mainloop()
