from tkinter import *

# creating a new window
window = Tk()
window.title("User Interface")
window.minsize(height=300, width=300)

# labels
title = Label(text="THE VIRTUAL GYM TRAINER")
title.grid(column=0,row=0)

# function to display bmi tab
def bmi_cal():
    confirm_button.destroy()
    bicepcurl.destroy()
    pushup.destroy()
    title.destroy()
    bmi_button.destroy()
    from bmi_calculator import calculate_bmi



#button for bmi calculator
bmi_button = Button(text="BMI calculator",command=bmi_cal)
bmi_button.grid(column=0,row=1)

def radio_used():
    print(radio_state.get())
    if radio_state.get() == 2:
        print("you selected pushups")

#radiobuttons
radio_state = IntVar()
bicepcurl = Radiobutton(text="Bicepcurl", value=1, variable=radio_state, command=radio_used)
bicepcurl.grid(column=0,row=2)

pushup = Radiobutton(text="Pushups", value=2, variable=radio_state, command=radio_used)
pushup.grid(column=0,row=3)

if radio_state == 2:
    print("you selected pushups")

# confirm_button
confirm_button = Button(text="confirm workout")
confirm_button.grid(column=0,row=4)



window.mainloop()