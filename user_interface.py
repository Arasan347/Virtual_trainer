from tkinter import *

# creating a new window
window = Tk()
window.title("User Interface")
window.minsize(height=300, width=300)

# labels
title = Label(text="THE VIRTUAL GYM TRAINER")
title.pack()


#button
bmi_button = Button(text="BMI calculator")
bmi_button.pack()

def radio_used():
    print(radio_state.get())
    if radio_state.get() == 2:
        print("you selected pushups")

#radiobuttons
radio_state = IntVar()
bicepcurl = Radiobutton(text="Bicepcurl", value=1, variable=radio_state, command=radio_used)
bicepcurl.pack()

pushup = Radiobutton(text="Pushups", value=2, variable=radio_state, command=radio_used)
pushup.pack()

if radio_state == 2:
    print("you selected pushups")

# confirm_button
confirm_button = Button(text="confirm workout")
confirm_button.pack()








window.mainloop()