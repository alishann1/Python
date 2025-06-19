import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import PIL


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("pygwidgets example")
        self.geometry("800x600")
        self.configure(bg='white')
        self.photo = tk.PhotoImage(file="Practice/pythonlogo.png")

        self.create_widgets()

    def create_widgets(self):

        image_label = tk.Label(self, image=self.photo,
                               bg="#a1c0d5")
        image_label.place(x=150, y=10)
        # Entry and label
        tk.Label(self, text="Default input text", bg='plum',
                 font=('Arial', 10, 'bold')).place(x=50, y=30)
        self.entry = tk.Entry(self, width=40)
        self.entry.insert(0, "Default input text")
        self.entry.place(x=50, y=60)

        # Drag label (simulated button)
        self.drag_label = tk.Label(
            self, text="DRAG\nME", bg="teal", fg="black", width=10, height=5, relief="raised")
        self.drag_label.place(x=350, y=60)

        # Centered text
        centered_text = "Here is some centered display text.\nShowing the\nnumber of frames.\nLoop counter: 95"
        tk.Label(self, text=centered_text, bg='plum',
                 justify="center").place(x=200, y=150)

        # Display text
        tk.Label(self, text="Here is some display text.  Loop counter:95",
                 font=('Arial', 10, 'bold'), bg='white').place(x=50, y=250)

        # Restart button
        self.restart_button = tk.Button(
            self, text="Restart", bg='teal', width=10)
        self.restart_button.place(x=150, y=280)

        # Checkboxes and radio buttons
        self.allow_radio_var = tk.IntVar(value=1)
        tk.Checkbutton(self, text="Allow radio btns",
                       variable=self.allow_radio_var, bg='teal').place(x=550, y=30)

        self.level_var = tk.StringVar(value="Med")
        tk.Radiobutton(self, text="Low", variable=self.level_var,
                       value="Low", bg='pink').place(x=550, y=60)
        tk.Radiobutton(self, text="Med", variable=self.level_var,
                       value="Med", bg='pink').place(x=550, y=90)
        tk.Radiobutton(self, text="High", variable=self.level_var,
                       value="High", bg='pink').place(x=550, y=120)

        self.allow_radio_2 = tk.IntVar(value=1)
        tk.Checkbutton(self, text="Allow Radio Buttons",
                       variable=self.allow_radio_2, bg='teal').place(x=550, y=170)

        self.radio_var = tk.StringVar(value="Radio Text 2")
        tk.Radiobutton(self, text="Radio Text 1", variable=self.radio_var,
                       value="Radio Text 1", bg='pink').place(x=570, y=200)
        tk.Radiobutton(self, text="Radio Text 2", variable=self.radio_var,
                       value="Radio Text 2", bg='pink').place(x=570, y=230)
        tk.Radiobutton(self, text="Radio Text 3", variable=self.radio_var,
                       value="Radio Text 3", bg='pink').place(x=570, y=260)

        # Status button
        tk.Button(self, text="Show Status", width=12).place(x=550, y=300)

        # START button
        # Load Python logo

        # Bottom instructions
        tk.Label(self, text="Click then up or down arrow to resize,\nleft or right arrow to rotate,\nh or v to flip horizontal or vertical",
                 bg='white', justify='left').place(x=50, y=480)

        tk.Label(self, text="Click then type l, r, d, u, s, or Space",
                 bg='white', justify='left').place(x=550, y=480)


if __name__ == "__main__":  # <-- FIXED
    app = MainApplication()
    app.mainloop()

# import tkinter as tk
# from tkinter import ttk
# import os


# class PygwidgetsApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("pygwidgets example by Irv Kalb")
#         self.geometry("800x600")
#         self.configure(bg='light grey')

#         self.create_widgets()

#     def create_widgets(self):

#         # ✅ Add image (Python logo)
#         image_path = "Task/pythonlogo.png"
#         if os.path.exists(image_path):
#             self.photo = tk.PhotoImage(file=image_path)
#             self.image_label = tk.Label(self, image=self.photo, bg="#a1c0d5")
#             self.image_label.place(x=150, y=10)
#         else:
#             print(f"❌ Image not found at: {image_path}")
#         # Default input label and entry
#         tk.Label(self, text="Default input text", bg='light grey',
#                  font=('Arial', 10, 'bold')).place(x=50, y=30)
#         self.entry = tk.Entry(self, width=40)
#         self.entry.insert(0, "Default input text")
#         self.entry.place(x=50, y=60)

#         # DRAG ME label
#         self.drag_label = tk.Label(
#             self, text="DRAG\nME", bg="gray", fg="black", width=10, height=5, relief="raised")
#         self.drag_label.place(x=350, y=60)

#         # Centered multi-line text
#         centered_text = "Here is some centered display text.\nShowing the\nnumber of frames.\nLoop counter: 95"
#         tk.Label(self, text=centered_text, bg='light grey',
#                  justify="center").place(x=200, y=150)

#         # Display text
#         tk.Label(self, text="Here is some display text.  Loop counter:95",
#                  font=('Arial', 10, 'bold'), bg='white').place(x=50, y=250)

#         # Restart button
#         self.restart_button = tk.Button(self, text="Restart", width=10)
#         self.restart_button.place(x=150, y=280)

#         # Checkbox and radio group (top right)
#         self.allow_radio_var = tk.IntVar(value=1)
#         tk.Checkbutton(self, text="Allow radio btns",
#                        variable=self.allow_radio_var, bg='light grey').place(x=550, y=30)

#         self.level_var = tk.StringVar(value="Med")
#         tk.Radiobutton(self, text="Low", variable=self.level_var,
#                        value="Low", bg='light grey').place(x=550, y=60)
#         tk.Radiobutton(self, text="Med", variable=self.level_var,
#                        value="Med", bg='light grey').place(x=550, y=90)
#         tk.Radiobutton(self, text="High", variable=self.level_var,
#                        value="High", bg='light grey').place(x=550, y=120)

#         self.allow_radio_2 = tk.IntVar(value=1)
#         tk.Checkbutton(self, text="Allow Radio Buttons",
#                        variable=self.allow_radio_2, bg='light grey').place(x=550, y=170)

#         self.radio_var = tk.StringVar(value="Radio Text 2")
#         tk.Radiobutton(self, text="Radio Text 1", variable=self.radio_var,
#                        value="Radio Text 1", bg='light grey').place(x=570, y=200)
#         tk.Radiobutton(self, text="Radio Text 2", variable=self.radio_var,
#                        value="Radio Text 2", bg='light grey').place(x=570, y=230)
#         tk.Radiobutton(self, text="Radio Text 3", variable=self.radio_var,
#                        value="Radio Text 3", bg='light grey').place(x=570, y=260)

#         # Show Status button
#         tk.Button(self, text="Show Status", width=12,
#                   command=self.show_status).place(x=550, y=300)

#         # START button
#         tk.Button(self, text="START", font=('Arial', 12, 'bold'),
#                   bg='light grey', width=15, height=2).place(x=550, y=400)

#         # Bottom instructions
#         tk.Label(self, text="Click then up or down arrow to resize,\nleft or right arrow to rotate,\nh or v to flip horizontal or vertical",
#                  bg='light grey', justify='left').place(x=50, y=480)
#         tk.Label(self, text="Click then type l, r, d, u, s, or Space",
#                  bg='light grey', justify='left').place(x=550, y=480)

#     def show_status(self):
#         print("Entry Text:", self.entry.get())
#         print("Level:", self.level_var.get())
#         print("Radio Selected:", self.radio_var.get())
#         print("Allow Radio 1:", self.allow_radio_var.get())
#         print("Allow Radio 2:", self.allow_radio_2.get())


# if __name__ == "__main__":
#     app = PygwidgetsApp()
#     app.mainloop()
