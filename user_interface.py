from tkinter import *

# creating a new window
window = Tk()
window.title("User Interface")
window.minsize(height=300, width=300)
window.config(padx=100,pady=50, background="#F0EB8D")


# labels
title = Label(text="THE VIRTUAL GYM TRAINER")
title.grid(column=1,row=2)
title.configure(font="Courier")
title.configure(padx=10,pady=10, background="#F0EB8D")

# function to display bmi tab
def bmi_cal():
    confirm_button.destroy()
    bicepcurl.destroy()
    shoulder_press.destroy()
    title.destroy()
    bmi_button.destroy()
    window.destroy()
    from bmi_calculator import calculate_bmi

def confirm():
    if radio_state.get() == 1:
        from main import Bicep_curl
    else:
        from shoulder_press import Shoulder



#button for bmi calculator
bmi_button = Button(text="BMI calculator",command=bmi_cal)
bmi_button.grid(column=1,row=3)
bmi_button.configure(background="blue")



#radiobuttons
radio_state = IntVar()
bicepcurl = Radiobutton(text="Bicepcurl", value=1, variable=radio_state)
bicepcurl.grid(column=1,row=4)
bicepcurl.configure(padx=10,pady=10, background="#F0EB8D")

shoulder_press = Radiobutton(text="Shoulder", value=2, variable=radio_state)
shoulder_press.grid(column=1, row=5)
shoulder_press.configure(padx=10,pady=10, background="#F0EB8D")

if radio_state == 2:
    print("you selected pushups")

# confirm_button
confirm_button = Button(text="confirm workout", command=confirm)
confirm_button.grid(column=1,row=6)
confirm_button.configure(background="red")



window.mainloop()