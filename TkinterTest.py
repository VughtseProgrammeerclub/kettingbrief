# als eerste installeren Tkinter en pandas en openpyxl met "pip install XXX"
import tkinter as tk
import pandas as pd
from tkinter import Canvas
from tkinter.filedialog import askopenfilename
#
def calculate_discount_percentage(total):
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    return discount
#
def calculate_getal(total):
    #print(total)
    getal_percentage = calculate_discount_percentage(total)
    getal = total - total / 100 * getal_percentage
    korting = total / 100 * getal_percentage
    return getal, korting, getal_percentage
#    
def get_verwerk_total():
    entered_verwerk_total = Invul.get()
    try:
        verwerk_total = float(entered_verwerk_total)
    except ValueError:
        textbox["text"] = "onjuiste waarde"
        textbox2["text"] = "          "
        return
    final_total, final_korting, Perc_korting = calculate_getal(verwerk_total)
    textbox["text"] = "€ " + format(final_total,'.2f')
    textbox2["text"] = "€ "+ format(final_korting, '.2f') + "   " + format(Perc_korting,'.0f') + "% korting"

def open_exel_file():
    filepath = askopenfilename(
        filetypes=[("Excel", "*.xlsx"), ("All Files", "*.*")]
    )
    if not filepath:
        return  
    # Open van het Excel bestand wat gekozen is
    df = pd.read_excel(filepath)
    # Verkrijgen van aantal rijen en kolommen
    n_rows, n_columns = get_number_rows_columns(df)
    # Verkrijgen van de maximale waarde
    max_value = get_highest_value(df)
    # Updaten van de labels
    update_labels(n_rows, n_columns, max_value)
    
# Hulpfunctie voor het verkrijgen van het aantal rijen en kolommen
def get_number_rows_columns(df):
    shape = df.shape
    n_rows = shape[0]
    n_columns = shape[1]
    return n_rows, n_columns
    
# Hulpfunctie voor het verkrijgen van de maximale waarde
def get_highest_value(df):
    max_value = df.max().max()
    return max_value

# Hulpfunctie om de labels te updaten
def update_labels(n_rows, n_columns, max_value):
    label_rows["text"] = f"Aantal rijen: {n_rows}"
    label_columns["text"] = f"Aantal kolommen: {n_columns}"
    label_max["text"] = f"Hoogste waarde: {max_value}"
    
#scherm
window = tk.Tk()
window.geometry("800x410")
window.title("Twee TKinter testjes")
window.columnconfigure([0], minsize=20)
window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], minsize=30)

lijn2 = tk.Label(text = " ")
lijn2.place(x = 10, y = 0, height = 25, width=750)
lijn2.config(bg="green")
lijn3 = tk.Label(text = "1.  Korting berekenen (10% onder 100, 20% boven 100")
lijn3.place(x = 10, y = 20, height = 25, width=750)
lijn3.config(bg="yellow", font="18")

# tekst in window
labelm = tk.Label(text = "Vul een bedrag in:  xx.xx")
labelm.place(x = 10, y = 50, height = 25)
labelm.config(bg="lightblue", padx=40)
# invulveld
Invul = tk.Entry(text = "")
Invul.place(x = 10, y = 80, width = 210, height = 25)
# knop verwerken
Knop = tk.Button(text="Verwerken", command = get_verwerk_total, relief="solid")
Knop.config(font="16")
Knop.place(x = 530,y = 75, width = 210, height = 35)
#
label2 = tk.Label(text = "Uitkomst:")
label2.place(x = 340, y = 50, height = 25)
label2.config(bg="lightblue", padx=40)
#
textbox = tk.Message(text = "", width = 200, font = "16")
textbox.config(bg="lightblue",padx = 0)
textbox.place(x = 340, y = 80)
#
textbox2 = tk.Message(text = "Totale korting: ", width = 500, font = "16")
textbox2.config(bg="pink", padx = 0)
textbox2.place(x = 340, y = 110)
#
#
#label.place(x = 340, y = 120, height = 25)
label_rows = tk.Label(text="Aantal rijen:")
label_columns = tk.Label(text="Aantal kolommen:")
label_max = tk.Label(text="Hoogste waarde:")
button_open = tk.Button(text='Open Excel file', width=20, command=open_exel_file, font = "20")
#button.place(x = 340, y = 250, height = 25)

label_rows.grid(row=7, column=0, sticky="w", padx=5, pady=5)
label_columns.grid(row=8, column=0, sticky="w", padx=5, pady=5)
label_max.grid(row=9, column=0, sticky="w", padx=5, pady=5)
button_open.grid(row=10, column=0, padx=5, pady=5)
button_open.config(font="16")

#Een lijn trekken
canvas=tk.Canvas(window)
#canvas=Canvas(window, width=500, height=300)
#canvas.pack()
canvas.place()
canvas.create_line(100,200,200,35, fill="green", width=5)

lijn = tk.Label(text = " ")
lijn.place(x = 10, y = 160, height = 25, width=750)
lijn.config(bg="green")
lijn1 = tk.Label(text = "2.  Analyseer een excel-spreadsheet")
lijn1.place(x = 10, y = 180, height = 25, width=750)
lijn1.config(bg="yellow", font="18")


window.mainloop()