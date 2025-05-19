import qiskit
import tkinter
from tkinter import LEFT

# Define window
root = tkinter.Tk()
root.title('Bloch Sphere')

# Set icon image
root.iconbitmap(default='logo.ico')
root.geometry('422x410')
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

x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X')
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y')
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z')
x_gate.grid(row=0, column=0,ipadx=48,ipady=1)
y_gate.grid(row=0, column=1,ipadx=48,ipady=1)
z_gate.grid(row=0, column=2,ipadx=60,ipady=1)

Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rx')
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Ry')
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rz')
Rx_gate.grid(row=1, column=0,columnspan=1,ipady=1,sticky='WE')
Ry_gate.grid(row=1, column=1,columnspan=1,ipady=1,sticky='WE')
Rz_gate.grid(row=1, column=2,columnspan=1,ipady=1,sticky='WE')

s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S')
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD')
h_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H')
s_gate.grid(row=2, column=0,columnspan=1,ipady=1,sticky='WE')
sd_gate.grid(row=2, column=1,columnspan=1,ipady=1,sticky='WE')
h_gate.grid(row=2, column=2,rowspan=2,ipady=1,sticky='WENS')

t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T')
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD')
t_gate.grid(row=3, column=0,sticky='WE')
td_gate.grid(row=3, column=1,sticky='WE')

quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='QUIT')
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='VISUALIZE')
quit.grid(row=4, column=0,sticky='WE',columnspan=2,ipadx=5)
visualize.grid(row=4, column=2,pady=1,sticky='WE',ipadx=8,columnspan=1)

# Main loop
root.mainloop()
