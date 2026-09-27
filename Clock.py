import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="black")

# Function to show time
def show_time():
    time = strftime("%H:%M:%S")
    clock.config(text=time)
    clock.after(1000, show_time)

# Digital clock
clock = tk.Label(
    root,
    font=("Arial", 50),
    bg="black",
    fg="green"
)

clock.pack(expand=True)

# Start clock
show_time()

# Run the program
root.mainloop()