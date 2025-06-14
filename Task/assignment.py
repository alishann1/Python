import tkinter as tk
from tkinter import ttk

# Main window
root = tk.Tk()
root.title("OOPS Assignment by Ali Shan")
root.geometry("800x600")
root.configure(bg='light grey')

# Default input label and entry
tk.Label(root, text="Default input text", bg='light grey',
         font=('Arial', 10, 'bold')).place(x=50, y=30)
entry = tk.Entry(root, width=40)
entry.insert(0, "Default input text")
entry.place(x=50, y=60)

# Drag me label (simulated as a button)
drag_label = tk.Label(root, text="DRAG\nME", bg="gray",
                      fg="black", width=10, height=5, relief="raised")
drag_label.place(x=350, y=60)

# Centered text (multi-line)
centered_text = "Here is some centered display text.\nShowing the\nnumber of frames.\nLoop counter: 95"
tk.Label(root, text=centered_text, bg='light grey',
         justify="center").place(x=200, y=150)

# Display text at bottom
tk.Label(root, text="Here is some display text.  Loop counter:95",
         font=('Arial', 10, 'bold'), bg='white').place(x=50, y=250)

# Restart button
restart_button = tk.Button(root, text="Restart", width=10)
restart_button.place(x=150, y=280)

# Checkbox: Allow radio btns (top right)
allow_radio_var = tk.IntVar(value=1)
tk.Checkbutton(root, text="Allow radio btns",
               variable=allow_radio_var, bg='light grey').place(x=550, y=30)

# Radio group: Low/Med/High
level_var = tk.StringVar(value="Med")
tk.Radiobutton(root, text="Low", variable=level_var,
               value="Low", bg='light grey').place(x=550, y=60)
tk.Radiobutton(root, text="Med", variable=level_var,
               value="Med", bg='light grey').place(x=550, y=90)
tk.Radiobutton(root, text="High", variable=level_var,
               value="High", bg='light grey').place(x=550, y=120)

# Another checkbox: Allow Radio Buttons
allow_radio_2 = tk.IntVar(value=1)
tk.Checkbutton(root, text="Allow Radio Buttons",
               variable=allow_radio_2, bg='light grey').place(x=550, y=170)

# Another set of radio buttons
radio_var = tk.StringVar(value="Radio Text 2")
tk.Radiobutton(root, text="Radio Text 1", variable=radio_var,
               value="Radio Text 1", bg='light grey').place(x=570, y=200)
tk.Radiobutton(root, text="Radio Text 2", variable=radio_var,
               value="Radio Text 2", bg='light grey').place(x=570, y=230)
tk.Radiobutton(root, text="Radio Text 3", variable=radio_var,
               value="Radio Text 3", bg='light grey').place(x=570, y=260)

# Show Status button
tk.Button(root, text="Show Status", width=12).place(x=550, y=300)

# START button (bottom right)
tk.Button(root, text="START", font=('Arial', 12, 'bold'),
          bg='light grey', width=15, height=2).place(x=550, y=400)

# Bottom instructions (left and right)
tk.Label(root, text="Click then up or down arrow to resize,\nleft or right arrow to rotate,\nh or v to flip horizontal or vertical",
         bg='light grey', justify='left').place(x=50, y=480)

tk.Label(root, text="Click then type l, r, d, u, s, or Space",
         bg='light grey', justify='left').place(x=550, y=480)

root.mainloop()
