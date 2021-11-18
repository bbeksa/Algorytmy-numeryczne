from tkinter import *

# Import functions
from tkinter import messagebox

from functions import *


def click_calculate():
    for widget in frame3.winfo_children():
        widget.destroy()

    input_function = str(entry_function.get())
    input_x0 = float(entry_x0.get())
    input_n = int(entry_n.get())

    if input_n < 1:
        messagebox.showerror("Złe dane", "Zmienna 'n' musi być większa bądź równa 1.")
        return

    try:
        result_text = str(round(count(input_function, input_x0, input_n), 5))
    except ValueError:
        messagebox.showerror("Złe dane", "Sprawdź czy funkja jest dobrze wprowadzona.")
        return

    if result_text == 'zoo':
        messagebox.showerror("Dzielenie przez zero", "Nie można obliczyć daną metodą.")
        return

    result_label = Label(frame3, text=result_text)
    result_label.grid(column=0, row=0)


root = Tk()
root.title("Metoda Newtona (stycznych)")
root.iconbitmap('grafika.ico')

frame = LabelFrame(root, text="Instrukcja", padx=5, pady=5)
frame.pack(padx=10, pady=10)

frame2 = LabelFrame(root, text="Podaj dane", padx=5, pady=5)
frame2.pack(padx=10, pady=10)

frame3 = LabelFrame(root, text="Wynik", padx=5, pady=5)
frame3.pack(padx=10, pady=10)

instruction_text = Label(frame, text="Jako zmiennej należy używać 'x'.\n"
                                     "Funkcja powinna być zapisana jak wyrażenie matematyczne w pythonie\n"
                                     "np. x² powinno być zapisane w postaci x**2\n"
                                     "      2x powinno być zapisane w postaci 2*x\n"
                                     "Zmienna 'n' musi być większa bądź równa 1.\n"
                                     "x₀ należy podać jako liczbę zmiennoprzecinkową", justify='left')
instruction_text.grid(column=0, row=0)

text_function = Label(frame2, text="f(x) = ", width=5)
entry_function = Entry(frame2, width=40)
text_function.grid(column=0, row=0)
entry_function.grid(column=1, row=0, sticky='w')

text_x0 = Label(frame2, text="x₀ = ", width=5)
entry_x0 = Entry(frame2, width=10)
text_x0.grid(column=0, row=1)
entry_x0.grid(column=1, row=1, sticky='w')

text_n = Label(frame2, text="n = ", width=5)
entry_n = Entry(frame2, width=10)
text_n.grid(column=0, row=2)
entry_n.grid(column=1, row=2, sticky='w')

button_calculate = Button(frame2, text='Oblicz', command=click_calculate, width=45)
button_calculate.grid(column=0, row=3, columnspan=2)

root.mainloop()
