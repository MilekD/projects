from tkinter import *
import tkinter.messagebox

#=================================Functions==================================================
def calculate_OH():
    equivalent = oh_equivalent.get()
    result = 56100 / equivalent
    oh_result.set(format(result, '.4f'))
    print(result)

def calculate_izocyanate():
    izocyanate_number = izocyanate_number_var.get()
    result = 42 * 100 / izocyanate_number
    izocyanate_result.set(format(result, '.4f'))
    print(result)

def calculate_water_mass():
    temperature = foam_temperature.get() + 273.15  # [K]
    volume = foam_volume.get() * 0.001  # [m^3]
    n_moles = (101300 * volume) / (8.314 * temperature)
    mass = n_moles * 18
    water_mass_result.set(format(mass, '.4f'))
    print(mass)

def calculate_isocyanate_demand():
    water_content = water_content_var.get()
    inco_index = inco_index_var.get()
    result = (100 / oh_result.get() + ((water_mass_result.get() * co2_content.get()) / 100 - water_content) / 9) * izocyanate_result.get() * inco_index
    isocyanate_demand_result.set(format(result, '.4f'))
    print(result)

def calculate_foam_mass():
    density = foam_density.get()
    volume = foam_volume.get()
    mass = volume * density
    foam_mass_result.set(format(mass, '.4f'))
    print(mass)

def calculate_polyol_amount():
    mass = foam_mass_result.get()
    isocyanate_demand = isocyanate_demand_result.get()
    polyol_amount = mass * 100 / (100 + isocyanate_demand)
    polyol_amount_result.set(format(polyol_amount, '.4f'))
    print(polyol_amount)

def calculate_isocyanate_amount():
    mass = foam_mass_result.get()
    polyol_amount = polyol_amount_result.get()
    isocyanate_amount = mass - polyol_amount
    isocyanate_amount_result.set(format(isocyanate_amount, '.4f'))
    print(isocyanate_amount)

def calculate_moles():
    temperature = foam_temperature.get() + 273.15  # [K]
    volume = foam_volume.get() * 0.001  # [m^3]
    n_moles = (101300 * volume) / (8.314 * temperature)
    moles_result.set(format(n_moles, '.4f'))
    print(n_moles)

def calculate_foaming_agent_mass():
    moles = moles_result.get()
    molar_mass = molar_mass_var.get()
    foaming_agent_mass = ((100 - co2_content.get()) * moles * molar_mass) / 100
    foaming_agent_mass_result.set(format(foaming_agent_mass, '.4f'))
    print(foaming_agent_mass)

def calculate_all():
    calculate_OH()
    calculate_izocyanate()
    calculate_water_mass()
    calculate_isocyanate_demand()
    calculate_foam_mass()
    calculate_polyol_amount()
    calculate_isocyanate_amount()
    calculate_moles()
    calculate_foaming_agent_mass()

def toggle_entry():
    global hidden
    if hidden:
        co2_entry.grid(row=8, column=1)
        co2_label.grid(row=8, column=0, sticky=E)
        co2_unit_label.grid(row=8, column=2, sticky=W)
        molar_mass_entry.grid(row=9, column=1)
        molar_mass_label.grid(row=9, column=0, sticky=E)
        molar_mass_unit_label.grid(row=9, column=2, sticky=W)
        foaming_agent_mass_label.grid(row=18, column=1, columnspan=1, sticky='WE')
        foaming_agent_mass_label_text.grid(row=18, column=0, sticky=E)
        foaming_agent_mass_unit_label.grid(row=18, column=2, sticky=W)
    else:
        co2_entry.grid_remove()
        co2_label.grid_remove()
        co2_unit_label.grid_remove()
        molar_mass_entry.grid_remove()
        molar_mass_label.grid_remove()
        molar_mass_unit_label.grid_remove()
        foaming_agent_mass_label.grid_remove()
        foaming_agent_mass_label_text.grid_remove()
        foaming_agent_mass_unit_label.grid_remove()
    hidden = not hidden

def display_info():
    tkinter.messagebox.showinfo("Info", "Program do liczenia receptur pianek (wersja demo).\n\nCreated by M.D.")

#=================================Root==================================================
root = Tk()
root.title('Pianex')
root.configure(bg='gray14')

#=================================Menu==================================================
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Info", menu=subMenu)
subMenu.add_command(label="Info", command=display_info)

#=================================Variables=============================================
oh_equivalent = DoubleVar()
izocyanate_number_var = DoubleVar()
foam_temperature = DoubleVar()
foam_volume = DoubleVar()
inco_index_var = DoubleVar()
water_content_var = DoubleVar()
foam_density = DoubleVar()
co2_content = DoubleVar(root, value=100)
molar_mass_var = DoubleVar()

oh_result = DoubleVar()
izocyanate_result = DoubleVar()
water_mass_result = DoubleVar()
isocyanate_demand_result = DoubleVar()
foam_mass_result = DoubleVar()
polyol_amount_result = DoubleVar()
isocyanate_amount_result = DoubleVar()
moles_result = DoubleVar()
foaming_agent_mass_result = DoubleVar()

#=================================Labels and Entries====================================
labels_and_entries = [
    ("Wartosc liczby hydroksylowej:", oh_equivalent, "mgOH/g"),
    ("Liczba izocyjanianowa:", izocyanate_number_var, "%"),
    ("Temperatura pianki:", foam_temperature, "°C"),
    ("Objetosc pianki:", foam_volume, "dm^3"),
    ("Indeks izocyjanianowy:", inco_index_var, "%"),
    ("Zawartosc wody w poliolu:", water_content_var, "%mas."),
    ("Gestosc pozorna:", foam_density, "kg/m^3")
]

for i, (label_text, var, unit) in enumerate(labels_and_entries):
    Label(root, text=label_text, font=("Helvetica", 9, "bold"), bg="gray14", fg="white").grid(row=i, sticky=E)
    Entry(root, textvariable=var, bg="pale goldenrod", fg="black").grid(row=i, column=1)
    Label(root, text=unit, bg="gray14", fg="white").grid(row=i, column=2, sticky=W)

#=================================CheckButton===========================================
hidden = True
Checkbutton(root, text='Inna zawartosc CO2', command=toggle_entry, bg="gray14", fg="white").grid(row=7, column=0)

co2_label = Label(root, text="Udzial CO2:", font=("Helvetica", 9, "bold"), bg="gray14", fg="white")
co2_entry = Entry(root, textvariable=co2_content, bg="pale goldenrod", fg="black")
co2_unit_label = Label(root, text="%", bg="gray14", fg="white")

molar_mass_label = Label(root, text="Masa molowa spieniacza:", font=("Helvetica", 9, "bold"), bg="gray14", fg="white")
molar_mass_entry = Entry(root, textvariable=molar_mass_var, bg="pale goldenrod", fg="black")
molar_mass_unit_label = Label(root, text="[g/mol]", bg="gray14", fg="white")

foaming_agent_mass_label_text = Label(root, text='Ilosc spieniacza:', font=("Helvetica", 9, "bold"), bg="gray14", fg="white")
foaming_agent_mass_label = Label(root, textvariable=foaming_agent_mass_result, relief='raised', bg="pale goldenrod")
foaming_agent_mass_unit_label = Label(root, text="[g]", bg="gray14", fg="white")

#=================================Calculation Labels====================================
calculation_labels = [
    ("Rownowaznik grup OH w KOH:", oh_result, "[g/mol]"),
    ("Rownowaznik grup izocyjanian.:", izocyanate_result, ""),
    ("Ilosc wody:", water_mass_result, "[g]"),
    ("Zap. na skl. izocyjanian.:", isocyanate_demand_result, "[g]"),
    ("Masa pianki:", foam_mass_result, "[g]"),
    ("Ilosc poliolu:", polyol_amount_result, "[g]"),
    ("Ilosc izocyjanianu:", isocyanate_amount_result, "[g]")
]

for i, (label_text, var, unit) in enumerate(calculation_labels, start=11):
    Label(root, text=label_text, font=("Helvetica", 9, "bold"), bg="gray14", fg="white").grid(row=i, column=0, sticky=E)
    Label(root, textvariable=var, relief='raised', bg="pale goldenrod", fg="black").grid(row=i, column=1, columnspan=1, sticky='WE')
    if unit:
        Label(root, text=unit, bg="gray14", fg="white").grid(row=i, column=2, sticky=W)

#=================================Button================================================
Button(root, text='OBLICZ', command=calculate_all, font=("Helvetica", 13, "bold"), bg="red3", fg="black").grid(row=10, column=1, padx=5, pady=5)

#=================================Run the application===================================
root.mainloop()
