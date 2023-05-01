from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("User Interface")
window.minsize(height=300, width=300)
window.config(padx=20, pady=30)

canvas = Canvas(width=200, height=200)
bmi_logo = PhotoImage(file="new_bmi.png")
canvas.create_image(100, 100, image=bmi_logo)
canvas.grid(column=0, row=0)

def calculate_bmi():
    cm = int(cm_input.get())
    kg = int(kg_input.get())
    the_BMI = round(kg / (cm/100)**2)
    if the_BMI <= 18.5:

        messagebox.showinfo(title="warning", message=f"Your Body Mass Index is {the_BMI}. Oops! You are underweight.")
    elif the_BMI <= 24.9:
        messagebox.showinfo(title="warning", message=f"Your Body Mass Index is {the_BMI}. Awesome! You are healthy.")
    elif the_BMI <= 29.9:
        messagebox.showinfo(title="warning", message=f"Your Body Mass Index is {the_BMI}. Eee! You are over weight.")
    else:
        messagebox.showinfo(title="warning", message=f"Your Body Mass Index is {the_BMI}. Seesh! You are obese.")

# labels
title = Label(text="BMI CALCULATOR", font="arial")
title.grid(column=1, row=0)


# asking inputs
cm_label = Label(text="Enter your height in cm: ")
cm_label.grid(column=0, row=1)

kg_label = Label(text="Enter your weight in kg: ")
kg_label.grid(column=0, row=2)

cm_input = Entry(width=10)
cm_input.grid(column=1, row=1)
cm_input.focus()

kg_input = Entry(width=10)
kg_input.grid(column=1, row=2)


cal_button = Button(text="CALCULATE BMI", command=calculate_bmi)
cal_button.grid(column=0, row=4)




window.mainloop()