1. Imports and Setup:
   - We import the necessary modules (`tkinter`, `Label`, and `time`).

2. `update_time` Function:
   - This function retrieves the current time using `time.strftime('%H:%M:%S')`, which formats the time in hours, minutes, and seconds.
   - The `clock_label.config(text=current_time)` updates the text of the label to display the current time.
   - The `clock_label.after(1000, update_time)` schedules the `update_time` function to be called again after 1000 milliseconds (1 second), creating a loop for continuous updating.

3. Creating the Main Window:
   - We create the main Tkinter window using `tk.Tk()` and set the title to 'Digital Clock'.

4. Creating the Clock Label:
   - We create a `Label` widget with a specific font, background color, and foreground color to display the time. The label is packed into the window using `pack(anchor='center')` to center it.

5. Initialize the Clock:
   - The `update_time` function is called once to initialize the clock display.

6. Start the Tkinter Event Loop:
   - Finally, we start the Tkinter event loop using `root.mainloop()`, which keeps the application running and responsive.

