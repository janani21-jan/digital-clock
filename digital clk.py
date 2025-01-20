import tkinter as tk
from tkinter import Label
import time

# Function to update the time every second
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update the clock every 1000 milliseconds (1 second)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Create a label to display the time
clock_label = Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
clock_label.pack(anchor='center')

# Call the update_time function to initialize the clock
update_time()

# Start the Tkinter event loop
root.mainloop()
