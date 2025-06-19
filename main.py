from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import FullAdderGate
from qiskit.visualization import visualize_transition
import tkinter
import numpy as np
from tkinter import LEFT, END, messagebox
import math

# Globals
THETA = 0

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

def clear_command():
    """
    Action for clear button, clears the queue for CIRCUIT
    and deletes the characters in input box.
    """
    CIRCUIT.data.clear()
    display.delete(0, END)

def help_command():
    """
    Action for help button, displays output box
    for help text to the user.
    """
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
    """
    Error checking for gates that have more than one letter
    as their symbol to ensure no more than 10 gates are applied.
    """
    display.insert(END, input)
    input_gates = display.get()
    num_pressed = len(input_gates)
    list_gates = list(input_gates)
    search_words = ["R", "D", "S", "T"]
    count_double_valued_gates = [list_gates.count(i) for i in search_words]
    num_pressed -= sum(count_double_valued_gates)
    if num_pressed == 10:
        gates = [x_gate, y_gate, z_gate, Rx_gate, Ry_gate, Rz_gate, s_gate, sd_gate, t_gate, td_gate, h_gate]
        for gate in gates:
            gate.config(state='disabled')


def change_theta(num, key):
    """
    Helper function for the R gates to get and transform
    the theta.
    """
    if num > 2 or num < -2 :
        messagebox.showerror('Float Error', 'Error: Please enter a number [-2, 2].')
        return
    THETA = num * np.pi
    if key == 'x':
        CIRCUIT.rx(THETA, 0)
        display_gate('Rx')
    elif key == 'y':
        CIRCUIT.ry(THETA, 0)
        display_gate('Ry')
    elif key == 'z':
        CIRCUIT.rz(THETA, 0)
        display_gate('Rz')
    THETA = 0

def adder_func(num1, num2):
    power = math.ceil(math.log2(max(num1, num2)))
    adder = FullAdderGate(power)

    reg_a = QuantumRegister(power, "A")
    number_a = QuantumCircuit(reg_a)
    number_a.initialize(num1, reg_a)

    reg_b = QuantumRegister(power, "B")
    number_b = QuantumCircuit(reg_b)
    number_b.initialize(num2, reg_b)

    # Main circuit with consistent sizes
    qregs = [
        QuantumRegister(1, "cin"),       # 1 qubit
        reg_a,                           # power qubits
        reg_b,                           # power qubits
        QuantumRegister(1, "cout")       # 1 qubit
    ]

    reg_result = ClassicalRegister(power)
    circuit_adder = QuantumCircuit(*qregs, reg_result)

    # Compose all pieces
    circuit_adder = (
        circuit_adder.compose(number_a, qubits=reg_a)
                    .compose(number_b, qubits=reg_b)
                    .compose(adder)
    )

    circuit_adder.measure(reg_b, reg_result)

    fig = circuit_adder.draw(output="mpl")
    fig.show()
    
def get_user_input(key):
    """
    Gets the user input for the R gates
    can be any real number [-2, 2] inclusive.
    """
    get_input = tkinter.Tk()
    get_input.title('Theta')
    get_input.geometry('300x300')
    get_input.resizable(0, 0)

    display_input = tkinter.LabelFrame(get_input)
    display_input.pack(pady=20)

    theta_screen = tkinter.Entry(display_input, width=20, font=display_font, bg=background, borderwidth=2, justify='left')
    theta_screen.pack(padx=3, pady=4)

    def on_submit():
        """
        Need to ensure that the input is
        a real number and not letters or
        other symbols.
        """
        try:
            theta_value = float(theta_screen.get())
            change_theta(theta_value, key)
            get_input.destroy()
        except ValueError:
            print("Please enter a valid real number.")
            messagebox.showerror('Float Error', 'Error: Please enter a valid value for Theta.')
            get_input.destroy()

    submit_button = tkinter.Button(get_input, text="Submit", command=on_submit)
    submit_button.pack()

    get_input.mainloop()

def get_user_nums():
    """
    Gets the user input for the R gates
    can be any real number [-2, 2] inclusive.
    """
    get_nums = tkinter.Tk()
    get_nums.title('Enter Numbers')
    get_nums.iconbitmap(default='logo.ico')
    get_nums.geometry('300x300')
    get_nums.resizable(0, 0)

    display_input = tkinter.LabelFrame(get_nums)
    display_input.pack(pady=20)

    num1_screen = tkinter.Entry(display_input, width=20, font=display_font, bg=background, borderwidth=2, justify='left')
    num1_screen.pack(padx=3, pady=4)

    num2_screen = tkinter.Entry(display_input, width=20, font=display_font, bg=background, borderwidth=2, justify='left')
    num2_screen.pack(padx=3, pady=4)

    def on_submit():
        """
        Need to ensure that the input is
        a real number and not letters or
        other symbols.
        """
        try:
            num1 = int(num1_screen.get())
            num2 = int(num2_screen.get())
            get_nums.destroy()
            adder_func(num1,num2)
        except ValueError:
            print("Please enter a valid real number.")
            messagebox.showerror('Float Error', 'Error: Please enter a valid value for Theta.')
            get_nums.destroy()

    submit_button = tkinter.Button(get_nums, text="Submit", command=on_submit)
    submit_button.pack()

    get_nums.mainloop()

def visualize_qubit():
    """
    The function doing the visualizing,
    given the circuit with the queue of gates applied
    prior to calling.
    """
    visualize_transition(CIRCUIT, trace=True,)

# Initialize the circuit
initialize_circuit()

# X, Y, Z gates
x_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='X',command=lambda:[display_gate('X'),CIRCUIT.x(0)])
y_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Y',command=lambda:[display_gate('Y'),CIRCUIT.y(0)])
z_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Z',command=lambda:[display_gate('Z'),CIRCUIT.z(0)])
x_gate.grid(row=0, column=0,ipadx=48,ipady=1)
y_gate.grid(row=0, column=1,ipadx=48,ipady=1)
z_gate.grid(row=0, column=2,ipadx=60,ipady=1)

# R gates
Rx_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rx',command=lambda:[get_user_input("x")])
Ry_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Ry',command=lambda:[get_user_input("y")])
Rz_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Rz',command=lambda:[get_user_input("z")])
Rx_gate.grid(row=1, column=0,columnspan=1,ipady=1,sticky='WE')
Ry_gate.grid(row=1, column=1,columnspan=1,ipady=1,sticky='WE')
Rz_gate.grid(row=1, column=2,columnspan=1,ipady=1,sticky='WE')

# S and H gates
s_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='S',command=lambda:[display_gate('S'),CIRCUIT.s(0)])
sd_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD',command=lambda:[display_gate('Sd'),CIRCUIT.sdg(0)])
h_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='H',command=lambda:[display_gate('H'),CIRCUIT.h(0)])
adder = tkinter.Button(button_frame, font=button_font, bg=buttons, text='Add',command=get_user_nums)
adder.grid(row=2, column=0,columnspan=1,ipady=1,sticky='WE')
s_gate.grid(row=2, column=1,columnspan=1,ipady=1,sticky='WE')
sd_gate.grid(row=2, column=2,columnspan=1,ipady=1,sticky='WE')
h_gate.grid(row=3, column=2,columnspan=1,ipady=1,sticky='WENS')

# T and TD gates
t_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='T',command=lambda:[display_gate('T'),CIRCUIT.t(0)])
td_gate = tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD',command=lambda:[display_gate('Td'),CIRCUIT.tdg(0)])
t_gate.grid(row=3, column=0,sticky='WE')
td_gate.grid(row=3, column=1,sticky='WE')

# Quit and visualizer buttons
quit = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='QUIT',command=root.destroy)
visualize = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='VISUALIZE',command=visualize_qubit)
quit.grid(row=4, column=2,sticky='WE',columnspan=1,ipadx=5)
visualize.grid(row=5,sticky='WE',ipadx=8,columnspan=3)

# Help and Clear
help = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='HELP', command=help_command)
clear = tkinter.Button(button_frame, font=button_font, bg=special_buttons, text='CLEAR', command=clear_command)
help.grid(row=4, column=0,sticky='WE',columnspan=2,ipadx=5)
clear.grid(row=6, column=0,pady=1,sticky='WE',ipadx=8,columnspan=3)

# Main loop
root.mainloop()
