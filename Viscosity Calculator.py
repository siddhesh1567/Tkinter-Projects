from tkinter import *


def viscocity():
    result = (float(e1.get()) * float(e3.get())) / float(e2.get())
    result = round(result, 4)
    label_text.set(result)


window = Tk()
window.geometry("450x300")
window.title('Coefficient of Viscocity Calculator')
label_text = StringVar();
Label(window, text='Coefficient of Viscocity Calculator').grid(row=0, column=1)
Label(window, text="").grid(row=1, column=0)
Label(window, text="τ :").grid(row=2, column=0)
Label(window, text="").grid(row=3, column=0)
Label(window, text="du :").grid(row=4, column=0)
Label(window, text="").grid(row=5, column=0)
Label(window, text="dy :").grid(row=6, column=0)
Label(window, text="").grid(row=7, column=0)
Label(window, text="Coefficient of Viscocity :").grid(row=10, column=0, padx=10)
result = Label(window, text="", textvariable=label_text).grid(row=10, column=1)
Label(window, text="Ns/m^2").grid(row=10, column=2, padx=10)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)

e1.grid(row=2, column=1)
e2.grid(row=4, column=1)
e3.grid(row=6, column=1)

b4 = Button(window, text="Calculate", width=10, command=viscocity)
b4.grid(row=8, column=1, padx=5, pady=5)
Label(window, text="").grid(row=9, column=0)

window.mainloop()