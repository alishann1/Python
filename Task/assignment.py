import tkinter as tk


class OOPSAssignmentApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("OOPS Assignment by Ali Shan")
        self.geometry("800x600")
        self.configure(bg="#a1c0d5")

        # Load the image (must be .png or .gif for PhotoImage)
        self.photo = tk.PhotoImage(file="Task/pythonlogo.png")

        self.create_widgets()

    def create_widgets(self):
        # Display the image
        image_label = tk.Label(self, image=self.photo,
                               bg="#a1c0d5")
        image_label.place(x=150, y=10)  # You can adjust x and y for placement

        tk.Label(self, text="Default input text", bg='#007acc',
                 fg='white', font=('Arial', 10, 'bold')).place(x=50, y=30)

        self.entry = tk.Entry(self, width=40, bg='white', fg='black')
        self.entry.insert(0, "Object Oriented Programming")
        self.entry.place(x=50, y=60)

        tk.Label(self, text="Registration number:", bg='#007acc',
                 fg='white', justify="center").place(x=200, y=120)

        tk.Label(self, text="2024-KIU-BS5698", bg="white",
                 fg="black", width=15, height=2, relief="raised").place(x=200, y=150)

        tk.Label(self, text="Karakoram International University",
                 font=('Arial', 10, 'bold'), bg='white').place(x=70, y=250)

        tk.Button(self, text="Press Me!", width=10,
                  bg='#007acc', fg='white').place(x=150, y=280)

        self.allow_radio_var = tk.IntVar(value=1)
        tk.Checkbutton(self, text="Allow radio btns",
                       variable=self.allow_radio_var, bg='#e0e0e0').place(x=550, y=30)

        self.level_var = tk.StringVar(value="Med")
        tk.Radiobutton(self, text="Low", variable=self.level_var,
                       value="Low", bg='#e0e0e0').place(x=550, y=60)
        tk.Radiobutton(self, text="Med", variable=self.level_var,
                       value="Med", bg='#e0e0e0').place(x=550, y=90)
        tk.Radiobutton(self, text="High", variable=self.level_var,
                       value="High", bg='#e0e0e0').place(x=550, y=120)

        self.allow_radio_2 = tk.IntVar(value=1)
        tk.Checkbutton(self, text="Allow Radio Buttons",
                       variable=self.allow_radio_2, bg='#e0e0e0').place(x=550, y=170)

        self.radio_var = tk.StringVar(value="Radio Text 2")
        tk.Radiobutton(self, text="Radio Text 1", variable=self.radio_var,
                       value="Radio Text 1", bg='#e0e0e0').place(x=550, y=200)
        tk.Radiobutton(self, text="Radio Text 2", variable=self.radio_var,
                       value="Radio Text 2", bg='#e0e0e0').place(x=550, y=230)
        tk.Radiobutton(self, text="Radio Text 3", variable=self.radio_var,
                       value="Radio Text 3", bg='#e0e0e0').place(x=550, y=260)

        tk.Button(self, text="Show Status", width=12,
                  bg='#007acc', fg='white').place(x=550, y=300)

        tk.Button(self, text="START", font=('Arial', 12, 'bold'),
                  bg='#007acc', fg='white', width=15, height=2).place(x=550, y=400)

        tk.Label(self, text="This is an assignment of OOPS completed by Ali Shan from BSCS A",
                 bg='#007acc', fg='white', justify='left').place(x=40, y=480)

        tk.Label(self, text="All of the buttons and text above is static and non-dynamic",
                 bg='#007acc', fg='white', justify='left').place(x=460, y=480)


if __name__ == "__main__":
    app = OOPSAssignmentApp()
    app.mainloop()
