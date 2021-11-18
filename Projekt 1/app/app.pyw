from tkinter import *

# Import functions
from tkinter import messagebox

from functions import *
from superscript import *

entries_x = []
entries_y = []


def click_number_of_pairs():
    for widget in frame2.winfo_children():
        widget.destroy()

    entries_x.clear()
    entries_y.clear()

    number_of_pairs = int(entry_number_of_pairs.get())

    if number_of_pairs >= 2:

        text_x = Label(frame2, text="x:")
        text_y = Label(frame2, text="y:")

        text_x.grid(column=1, row=1, columnspan=2)
        text_y.grid(column=3, row=1, columnspan=2)

        for count in range(number_of_pairs):
            index_label = Label(frame2, text=str(count) + ": ", width=2)
            en_x = Entry(frame2, width=13)
            en_y = Entry(frame2, width=13)

            index_label.grid(column=0, row=count + 2)
            en_x.grid(column=1, row=count + 2, columnspan=2)
            en_y.grid(column=3, row=count + 2, columnspan=2)

            entries_x.append(en_x)
            entries_y.append(en_y)

        button_calculate = Button(frame2, text="Oblicz", command=calculate, width=30)
        button_calculate.grid(column=0, row=number_of_pairs + 2, columnspan=5)


def calculate():
    for widget in frame3.winfo_children():
        widget.destroy()

    list_x = [float(x.get()) for x in entries_x]
    list_y = [float(y.get()) for y in entries_y]

    if len(list_x) != len(set(list_x)):
        messagebox.showerror("Złe dane!", "x nie może przyjmować takich samych wartości")
        return

    result = newtons_polynomial_interpolation(list_x, list_y)
    result.reverse()

    result_text = "P(x) = "

    first_number = True
    for index in reversed(range(len(result))):
        if index == 0:
            if result[index] != 0:
                if result[index] < 0:
                    result_text += str(round(result[index], 2))
                else:
                    if first_number:
                        result_text += str(round(result[index], 2))
                        first_number = False
                    else:
                        result_text += "+" + str(round(result[index], 2))
        elif index == 1:
            if result[index] != 0:
                if result[index] < 0:
                    result_text += str(round(result[index], 2)) + "x"
                else:
                    if first_number:
                        result_text += str(round(result[index], 2)) + "x"
                        first_number = False
                    else:
                        result_text += "+" + str(round(result[index], 2)) + "x"
        else:
            if result[index] != 0:
                if result[index] < 0:
                    result_text += str(round(result[index], 2)) + "x" + get_super(str(index))
                else:
                    if first_number:
                        result_text += str(round(result[index], 2)) + "x" + get_super(str(index))
                        first_number = False
                    else:
                        result_text += "+" + str(round(result[index], 2)) + "x" + get_super(str(index))

    result_label = Label(frame3, text=result_text)
    result_label.grid(column=0, row=3 + len(list_x), columnspan=5)


root = Tk()
root.title("Interpolacja wielomianowa metodą Newtona")
root.iconbitmap('grafika.ico')

frame = LabelFrame(root, text="Podaj liczbę par: ", padx=5, pady=5)
frame.pack(padx=10, pady=10)

frame2 = LabelFrame(root, text="Podaj pary x, y", padx=5, pady=5)
frame2.pack(padx=10, pady=10)

frame3 = LabelFrame(root, text="Wynik:", padx=5, pady=5)
frame3.pack(padx=10, pady=10)

# text_number_of_pairs = Label(root, text="Podaj liczbę par: ", width=15)
# text_number_of_pairs.grid(column=0, row=0, columnspan=3)

entry_number_of_pairs = Entry(frame, width=10)
entry_number_of_pairs.grid(column=0, row=0)

button_number_of_pairs = Button(frame, text="Dalej", command=click_number_of_pairs, width=5)
button_number_of_pairs.grid(column=1, row=0)


root.mainloop()
