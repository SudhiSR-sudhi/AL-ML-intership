import os
import tkinter as tk

# Get the directory where THIS script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "2.png")

root = tk.Tk()

# Pass the dynamic path to PhotoImage
photo = tk.PhotoImage(file=image_path)
label = tk.Label(root, image=photo)
label.pack()

root.mainloop()