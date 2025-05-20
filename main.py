import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import visualize_transition
import tkinter
from tkinter import LEFT, END

# Define window
root = tkinter.Tk()
root.title('Bloch Sphere')

# Set icon image
root.iconbitmap(default='logo.ico')
root.geometry('424x424')
root.resizable(0,0) # No resizing

# Define constants
background = '#2c94c8'
buttons = '#834558'
special_buttons = '#bc3454'
button_font = ('Arial', 18)
display_font = ('Arial', 32)

# Define frames & layouts
display_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root,bg='black')
display_frame.pack()
button_frame.pack(fill='both', expand=True)

# What you see when you type
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify=LEFT)
display.pack(padx=3, pady=4)

# Define functions
def initialize_circuit():
    """
    Initializes Quantum Circuit
    Could get rid of global vars
    """
    global CIRCUIT
    CIRCUIT = QuantumCircuit(1)

initialize_circuit()
theta = 0

def help_command():
    info = tkinter.Tk()
    info.title('Help')
    info.geometry('730x470')
    info.resizable(0,0)

    text = tkinter.Text(info, height=20,width=20)
    label = tkinter.Label(info, text = "🧠 Bloch Sphere Simulator – Help Guide")
    label.config(font= ("Arial", 14))

    text_to_display = """
    🎯 Purpose
    This simulator is designed to help users (especially students and educators) 
    understand the geometric interpretation of quantum gates by showing how each 
    operation transforms a qubit’s state on the Bloch Sphere.

    ▶️ Gate Buttons
    X, Y, Z – Pauli gates:

    X: Bit-flip gate (rotates qubit 180° about the X-axis).
    Y: Rotates about the Y-axis.
    Z: Phase-flip gate (rotates about the Z-axis).
    Rx, Ry, Rz – Rotation gates: Apply continuous rotation around X, Y, or Z axes [-2PI, 2PI]

    S, SD (S-dagger) – Phase gates:
    S: Adds a π/2 phase.
    SD: Inverse of the S gate.

    T, TD (T-dagger) – π/4 phase gates:
    T: Adds a π/4 phase.
    TD: Inverse of the T gate.

    H – Hadamard gate: Creates superposition: places qubit on the
    equator of the Bloch Sphere.

    📦 Utility Buttons
    QUIT – Exit the program.
    VISUALIZE – Show the current qubit state on the Bloch Sphere after all applied gates.
    HELP – Displays this help guide.
    CLEAR – Reset the qubit to its initial |0⟩ state and clear the gate history.

    🧪 How to Use
    Start with a qubit in state |0⟩.
    Press any gate button(s) in the desired order. The sequence is recorded.
    Click VISUALIZE to see the updated qubit state on the Bloch Sphere.
    Use CLEAR to start fresh or QUIT to exit.

    🧰 Troubleshooting
    Nothing appears on the sphere? Ensure you've pressed VISUALIZE after applying gates.
    Accidental inputs? Use the CLEAR button.
    Program frozen? Close the window and relaunch.
    """
    label.pack()
    text.pack(fill='both',expand=True)

    text.insert(END, text_to_display)

    info.mainloop()

def display_gate(input):
    display.insert(END, input)
    input_gates = display.get()
    num_pressed = len(input_gates)
    list_gates = list(input_gates)
    search_words = ["R", "D"]
    count_double_valued_gates = [list_gates.count(i) for i in search_words]
    num_pressed -= sum(count_double_valued_gates)
    if num_pressed == 10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, h_gate]
        for gate in gates:
            gate.config(state='disabled')

# X, Y, Z gates
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X',command=lambda:[display_gate('X'),CIRCUIT.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y',command=lambda:[display_gate('Y'),CIRCUIT.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z',command=lambda:[display_gate('Z'),CIRCUIT.z(0)])
x_gate.grid(row=0, column=0,ipadx=48,ipady=1)
y_gate.grid(row=0, column=1,ipadx=48,ipady=1)
z_gate.grid(row=0, column=2,ipadx=60,ipady=1)

# R gates
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rx',command=lambda:[display_gate('Rx'),CIRCUIT.x(0)])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Ry',command=lambda:[display_gate('Ry'),CIRCUIT.x(0)])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rz',command=lambda:[display_gate('Rz'),CIRCUIT.x(0)])
Rx_gate.grid(row=1, column=0,columnspan=1,ipady=1,sticky='WE')
Ry_gate.grid(row=1, column=1,columnspan=1,ipady=1,sticky='WE')
Rz_gate.grid(row=1, column=2,columnspan=1,ipady=1,sticky='WE')

# S and H gates
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S',command=lambda:[display_gate('S'),CIRCUIT.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD',command=lambda:[display_gate('Sd'),CIRCUIT.sdg(0)])
h_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H',command=lambda:[display_gate('H'),CIRCUIT.h(0)])
s_gate.grid(row=2, column=0,columnspan=1,ipady=1,sticky='WE')
sd_gate.grid(row=2, column=1,columnspan=1,ipady=1,sticky='WE')
h_gate.grid(row=2, column=2,rowspan=2,ipady=1,sticky='WENS')

# T and TD gates
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T',command=lambda:[display_gate('T'),CIRCUIT.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD',command=lambda:[display_gate('Td'),CIRCUIT.tdg(0)])
t_gate.grid(row=3, column=0,sticky='WE')
td_gate.grid(row=3, column=1,sticky='WE')

# Quit and visualizer buttons
quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='QUIT',command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='VISUALIZE')
quit.grid(row=4, column=0,sticky='WE',columnspan=2,ipadx=5)
visualize.grid(row=4, column=2,pady=1,sticky='WE',ipadx=8,columnspan=1)

# Help and Clear
help = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='HELP', command=help_command)
clear = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='CLEAR')
help.grid(row=5, column=0,sticky='WE',columnspan=3,ipadx=5)
clear.grid(row=6, column=0,pady=1,sticky='WE',ipadx=8,columnspan=3)

# Main loop
root.mainloop()
