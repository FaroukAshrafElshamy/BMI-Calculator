import ttkbootstrap as ttk

def Bmi():

    weight = entry.get()

    height = Entry1.get()

    try:

        if float(weight) > 0 or float(height) > 0:
            calc =  float(weight) / ((float(height)/100)**2)

            if calc < 18.5:

                output = f" you are Underweight  كل كويس يا حبيبي "

                output_string.set(output)

            elif calc >= 18.5 and calc < 25:

                output = f" Your weight is Ideal  انت عودك فرنساوي"

                output_string.set(output)

            else:

                output = f"Your are Over weight قم بتخسيس الكروش "

                output_string.set(output)
            
        else:

            output_string.set("⚠️ Enter Correct values")

    except ValueError:

        output_string.set("⚠️ Enter Correct values")


def clear(*args):

    if entry.get() == "Your weight in KG":

        entry.delete(0,"end")


def clear1(a):

    if Entry1.get() == "Your height in CM":

        Entry1.delete(0,"end")


def leave(*args):

    if entry.get() == "":

        entry.delete(0,"end")

        entry.insert(0,"Your weight in KG")
        window.focus()
        

    if Entry1.get() == "":

        Entry1.delete(0,"end")

        Entry1.insert(0,"Your height in CM")
        window.focus()


# window

window = ttk.Window(themename = "journal")

window.title("BMI")

window.geometry('650x280')


# title

title_label = ttk.Label(master= window , text = 'BMI Calculator 💪🏼',font = 'Calibri 24 bold')
title_label.pack()


# input field

input_frame = ttk.Frame(master = window)

entry = ttk.Entry(master = input_frame ,cursor = 'ibeam',width=60)

Entry1 = ttk.Entry(master = input_frame ,cursor = 'ibeam',width=60)

button = ttk.Button(master = input_frame , text = "Calculate" ,cursor = 'circle' ,command =Bmi,style='outline.primary')


entry.delete(0,'end')

Entry1.delete(0,'end')


entry.insert(0,"Your weight in KG")

Entry1.insert(0,"Your height in CM")


entry.bind("<Button>",clear)

entry.bind("<Leave>",leave)


Entry1.bind("<Button>",clear1)

Entry1.bind("<Leave>",leave)


entry.pack(side = 'top')

Entry1.pack(side = 'top', pady = 10 )


button.pack(side = 'top')

input_frame.pack(pady = 15)


# output 

output_string = ttk.StringVar()

output_label = ttk.Label(
    master = window, 

    text = 'Output',

    font = 'Calibri 20 bold',

    textvariable = output_string)

output_label.pack(pady = 5)


# Logo

Logo = ttk.PhotoImage(file = "icon.png")
window.iconphoto(False,Logo)

#Run
window.mainloop()


