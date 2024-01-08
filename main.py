from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=50)
window.config(padx=20, pady=20)




def convert():
    miles = float(input.get())
    converted_num = (miles * 1.61)
    my_label2["text"] = converted_num
    

input = Entry(width=10)
input.grid(column=1, row=0)

font_spec = ("Arial", 15,"bold")
my_label = Label(text="Miles", font=font_spec)
my_label.grid(column=2, row=0)

my_label1 = Label(text="is equal to", font=font_spec)
my_label1.grid(column=0, row=1)

my_label2 = Label(text="0", font=font_spec)
my_label2.grid(column=1, row=1)

km = Label(text="km", font=font_spec)
km.grid(column=2, row=1)

button = Button(text="calculate", command=convert)
button.grid(column=1,row=2)

window.mainloop()
