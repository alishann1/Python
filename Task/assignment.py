import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("OOPS Assignment by Ali Shan")
root.geometry("800x600")
root.configure(bg="#a1c0d5")

tk.Label(root, text="Default input text", bg='#007acc',
         fg='white', font=('Arial', 10, 'bold')).place(x=50, y=30)
entry = tk.Entry(root, width=40, bg='white', fg='black')
entry.insert(0, "Object Oriented Programming")
entry.place(x=50, y=60)

centered_text = "Registration number:"
tk.Label(root, text=centered_text, bg='#007acc',
         fg='white', justify="center").place(x=200, y=120)

drag_label = tk.Label(root, text="2024-KIU-BS5698", bg="white",
                      fg="black", width=15, height=2, relief="raised")
drag_label.place(x=200, y=150)

tk.Label(root, text="Karakoram International University",
         font=('Arial', 10, 'bold'), bg='white').place(x=70, y=250)

restart_button = tk.Button(root, text="Press Me!",
                           width=10, bg='#007acc', fg='white')
restart_button.place(x=150, y=280)

allow_radio_var = tk.IntVar(value=1)
tk.Checkbutton(root, text="Allow radio btns",
               variable=allow_radio_var, bg='#e0e0e0').place(x=550, y=30)

level_var = tk.StringVar(value="Med")
tk.Radiobutton(root, text="Low", variable=level_var,
               value="Low", bg='#e0e0e0').place(x=550, y=60)
tk.Radiobutton(root, text="Med", variable=level_var,
               value="Med", bg='#e0e0e0').place(x=550, y=90)
tk.Radiobutton(root, text="High", variable=level_var,
               value="High", bg='#e0e0e0').place(x=550, y=120)

allow_radio_2 = tk.IntVar(value=1)
tk.Checkbutton(root, text="Allow Radio Buttons",
               variable=allow_radio_2, bg='#e0e0e0').place(x=550, y=170)

radio_var = tk.StringVar(value="Radio Text 2")
tk.Radiobutton(root, text="Radio Text 1", variable=radio_var,
               value="Radio Text 1", bg='#e0e0e0').place(x=550, y=200)
tk.Radiobutton(root, text="Radio Text 2", variable=radio_var,
               value="Radio Text 2", bg='#e0e0e0').place(x=550, y=230)
tk.Radiobutton(root, text="Radio Text 3", variable=radio_var,
               value="Radio Text 3", bg='#e0e0e0').place(x=550, y=260)

tk.Button(root, text="Show Status", width=12,
          bg='#007acc', fg='white').place(x=550, y=300)

tk.Button(root, text="START", font=('Arial', 12, 'bold'),
          bg='#007acc', fg='white', width=15, height=2).place(x=550, y=400)

tk.Label(root, text="This is an assignment of OOPS completed by Ali Shan from BSCS A",
         bg='#007acc', fg='white', justify='left').place(x=40, y=480)

tk.Label(root, text="All of the buttons and text above is static and non-dynamic",
         bg='#007acc', fg='white', justify='left').place(x=460, y=480)

root.mainloop()
