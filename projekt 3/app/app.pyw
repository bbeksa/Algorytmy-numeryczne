from tkinter import *
from tkinter import messagebox
from functions import *

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
entries = []


def click_unknowns():
    for widget in frame2.winfo_children():
        widget.destroy()

    entries.clear()

    number_of_unknowns = int(entry_number_of_pairs.get())

    if number_of_unknowns >= 2:
        for i in range(number_of_unknowns):
            entries.append([0] * (number_of_unknowns + 1))
            for j in range(number_of_unknowns + 1):
                entries[i][j] = Entry(frame2, width=10)
                entries[i][j].grid(column=2 * j, row=i)
                if j < number_of_unknowns - 1:
                    string_x = result_label = Label(frame2, text=f'x{j} + '.translate(SUB))
                    string_x.grid(column=2 * j + 1, row=i)
                elif j == number_of_unknowns - 1:
                    string_x = result_label = Label(frame2, text=f'x{j} = '.translate(SUB))
                    string_x.grid(column=2 * j + 1, row=i)

        button_calculate = Button(frame2, text="Oblicz", command=calculate, width=10)
        button_calculate.grid(column=0, row=number_of_unknowns, columnspan=(number_of_unknowns + 1) * 2)


def calculate():
    for widget in frame3.winfo_children():
        widget.destroy()

    calculate_list = []

    try:
        number_of_unknowns = int(entry_number_of_pairs.get())
        for i in range(number_of_unknowns):
            calculate_list.append([0] * (number_of_unknowns + 1))
            for j in range(number_of_unknowns + 1):
                calculate_list[i][j] = float(entries[i][j].get())
    except ValueError:
        messagebox.showerror("Error", "Sprawdź poprawność wpisanych danych.\nPamiętaj aby wypełnić wszystkie pola.")
        return

    try:
        result = gauss_elimination(calculate_list, number_of_unknowns)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Dzielenie przez 0.")
        return

    result_text = ""

    for i in range(number_of_unknowns - 1):
        result_text += f'x{i} = '.translate(SUB)
        result_text += f'{round(result[i], 2)}\n'

    result_text += f'x{number_of_unknowns - 1} = '.translate(SUB)
    result_text += f'{round(result[number_of_unknowns - 1], 2)}'

    result_label = Label(frame3, text=result_text, justify=LEFT)
    result_label.grid(column=0, row=0, columnspan=5)


root = Tk()
root.title("Metoda Eliminacji Gaussa")

frame = LabelFrame(root, text="Liczba zmiennych: ", padx=5, pady=5)
frame.pack(padx=10, pady=10)

frame2 = LabelFrame(root, text="Równania:", padx=5, pady=5)
frame2.pack(padx=10, pady=10)

frame3 = LabelFrame(root, text="Wynik:", padx=5, pady=5)
frame3.pack(padx=10, pady=10)

entry_number_of_pairs = Entry(frame, width=10)
entry_number_of_pairs.grid(column=0, row=0)

button_number_of_pairs = Button(frame, text="Dalej", command=click_unknowns, width=5)
button_number_of_pairs.grid(column=1, row=0)

root.mainloop()
