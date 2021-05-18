# Import the 'tkinter module
import string
import tkinter
from tkinter import *
from tkinter.tix import ComboBox
from tkinter.ttk import Combobox

root = Tk()  # Blank window
root.geometry("1000x800")  # root window
# adding background colour
root.config(bg='pink')
# Can't change the size and shape of the window
root.resizable(width=False, height=False)  # The set size cannot be changed
# Title for the window
root.title("BMI-Calculator")

# Labels
label_weight = tkinter.Label(root, text="Weight:")
label_weight.place(x=50, y=50, width=180)
Label_height = tkinter.Label(root, text="Height:")
Label_height.place(x=50, y=75, width=180)
Label_gender = tkinter.Label(root, text="Gender:")
Label_gender.place(x=50, y=115, width=180)
Label_age = tkinter.Label(root, text="Age:")
Label_age.place(x=50, y=250)
Label_BMI = tkinter.Label(root, text="BMI:")
Label_BMI.place(x=50, y=350)
Label_ideal = tkinter.Label(root, text="Ideal-BMI")
Label_ideal.place(x=50, y=310)

# Textboxes
Input_weight = tkinter.Entry(root)
Input_weight.place(x=250, y=50, width=180)
Input_height = tkinter.Entry(root)
Input_height.place(x=250, y=70, width=180)
Input_age = tkinter.Entry(root)
Input_age.place(x=250, y=250)
Input_BMI = tkinter.Entry(root)
Input_BMI.place(x=250, y=350, width=180)
Input_ideal = tkinter.Entry(root)
Input_ideal.place(x=250, y=295)

# Combobox creation
Combobox = Combobox(root, values=['Female', 'Male'])
Combobox.place(x=250, y=115, width=180)

def button_clear():

    #CLEARING THE INPUT FIELDS
    Input_BMI.delete(0, END)
    Input_ideal.delete(0,END)
    Input_age.delete(0,END)
    Input_height.delete(0, END)
    Input_weight.delete(0, END)


def BMI_button():
    right_weight = float(Input_weight.get())
    right_height = float(Input_height.get())
    correct_BMI = right_weight / (right_height / 100) ** 2
    Input_BMI.insert(0, correct_BMI)


def Age ():
    get_age = int (Input_age.get())
    print("Age:" + get_age)

def button_exit(): #When the user presses 'exit', a popup box to ask the user whether they really want to exit will show up
    # EXITING
    import sys
    sys.exit()
    # exits the program


#Getting the selected gender from the Combobox
def getSelection():
    val = Combobox.get() #Getting the selected gender type
    # val = StringVar ()
    Input_ideal.insert(0, val)
    print(val)

def Ideal_button ():
    right_weight = float(Input_weight.get())
    right_height = float(Input_height.get())
    get_age = float (Input_age.get())
    val = Combobox.get() #Getting the selected gender type
    if val == "Female":
        correct_BMI = 0.5 * right_weight / (right_height / 100) ** 2 + 0.03 * get_age + 11
        Input_ideal.insert(0, correct_BMI)
    elif val == "Male":
        correct_BMI = 0.5 * right_weight / (right_height / 100) ** 2 + 0.03 * get_age + 11
        Input_ideal.insert(0, correct_BMI)
    else:
        print("This is an error")


# Buttons
Ideal_button = Button (root, borderwidth=10, font=("Consolas 10 bold"), text="Ideal-BMI", bg="green", fg="white",width=35, command=Ideal_button)
Ideal_button.place(x=300, y=550)
BMI_button = Button(root, borderwidth=10, font=("Consolas 10 bold"), text="BMI-Calculate", bg="green", fg="white",width=35, command=BMI_button)
BMI_button.place(x=300, y=500, width=350)
button_exit = Button(root, text="Exit", borderwidth=10, font=("Consolas 10 bold"), bg="green", fg="white", width=10, command=button_exit)
button_exit.place(x=170, y=550)
button_clear = Button(root, borderwidth=10, font=("Consolas 10 bold"), text="Clear", bg="green", fg="white", width=10, command=button_clear)
button_clear.place(x=170, y=500)

root.mainloop()
