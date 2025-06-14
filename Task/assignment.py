import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("OOPS Assignment by Ali Shan")
root.geometry("800x600")
root.configure(bg='light blue')

# Default input label and entry
tk.Label(root, text="Default input text", bg='orange',
         font=('Arial', 10, 'bold')).place(x=50, y=30)
entry = tk.Entry(root, width=40)
entry.insert(0, "Object Oriented Programming")
entry.place(x=50, y=60)

# Centered text (multi-line)
centered_text = "Registration number:"
tk.Label(root, text=centered_text, bg='orange',
         justify="center").place(x=200, y=120)

# Drag me label (simulated as a button)
drag_label = tk.Label(root, text="2024-KIU-BS5698", bg="white",
                      fg="black", width=15, height=2, relief="raised")
drag_label.place(x=200, y=150)

# Display text at bottom
tk.Label(root, text="Karakoram International University",
         font=('Arial', 10, 'bold'), bg='white').place(x=70, y=250)

# Restart button
restart_button = tk.Button(root, text="Press Me!", width=10)
restart_button.place(x=150, y=280)

# Checkbox: Allow radio btns (top right)
allow_radio_var = tk.IntVar(value=1)
tk.Checkbutton(root, text="Allow radio btns",
               variable=allow_radio_var, bg='orange').place(x=550, y=30)

# Radio group: Low/Med/High
level_var = tk.StringVar(value="Med")
tk.Radiobutton(root, text="Low", variable=level_var,
               value="Low", bg='orange').place(x=550, y=60)
tk.Radiobutton(root, text="Med", variable=level_var,
               value="Med", bg='orange').place(x=550, y=90)
tk.Radiobutton(root, text="High", variable=level_var,
               value="High", bg='orange').place(x=550, y=120)

# Another checkbox: Allow Radio Buttons
allow_radio_2 = tk.IntVar(value=1)
tk.Checkbutton(root, text="Allow Radio Buttons",
               variable=allow_radio_2, bg='orange').place(x=550, y=170)

# Another set of radio buttons
radio_var = tk.StringVar(value="Radio Text 2")
tk.Radiobutton(root, text="Radio Text 1", variable=radio_var,
               value="Radio Text 1", bg='orange').place(x=550, y=200)
tk.Radiobutton(root, text="Radio Text 2", variable=radio_var,
               value="Radio Text 2", bg='orange').place(x=550, y=230)
tk.Radiobutton(root, text="Radio Text 3", variable=radio_var,
               value="Radio Text 3", bg='orange').place(x=550, y=260)

# Show Status button
tk.Button(root, text="Show Status", width=12).place(x=550, y=300)

# START button (bottom right)
tk.Button(root, text="START", font=('Arial', 12, 'bold'),
          bg='orange', width=15, height=2).place(x=550, y=400)

# Bottom instructions (left and right)
tk.Label(root, text="This is an assignment of OOPS completed by Ali Shan from BSCS A",
         bg='orange', justify='left').place(x=40, y=480)

tk.Label(root, text="All of the buttons and text above is static and non-dynamic",
         bg='orange', justify='left').place(x=460, y=480)

root.mainloop()
