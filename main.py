import qiskit
import tkinter
from tkinter import LEFT

# Define window
root = tkinter.Tk()
root.title('Bloch Sphere')

# Set icon image
root.iconbitmap(default='logo.ico')
root.geometry('399x410')
root.resizable(0,0) # No resizing

# Define constants
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 32)

# Define functions


# Define layout

# Define frames
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

# What you see when you type
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify=LEFT)
display.pack(padx=3, pady=4)

# Main loop
root.mainloop()
