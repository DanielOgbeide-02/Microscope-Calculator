import tkinter as tk
from tkinter import messagebox
from database import init_db, save_measurement   # code above

init_db()

root = tk.Tk()
root.title("Microscope Size Calculator")

tk.Label(root, text="Username").grid(row=0, column=0)
tk.Label(root, text="Image size (mm)").grid(row=1, column=0)
tk.Label(root, text="Magnification (×)").grid(row=2, column=0)

u = tk.Entry(root); mm = tk.Entry(root); mag = tk.Entry(root)
u.grid(row=0, column=1); mm.grid(row=1, column=1); mag.grid(row=2, column=1)

def calculate():
    try:
        act = save_measurement(u.get(),
                               float(mm.get()),
                               float(mag.get()))
        messagebox.showinfo("Result", f"Actual size ≈ {act:.2f} µm\nSaved to DB.")
    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values.")

tk.Button(root, text="Calculate & Save", command=calculate).grid(row=3, columnspan=2, pady=5)
root.mainloop()
