import tkinter as tk


def calculate():
    kms = float(input.get()) * 1.609
    km_value.config(text=kms)


window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

# Labels
Miles = tk.Label(text="Miles", font=("Arial",24,"bold"))
Miles.grid(column=3,row=1)
is_equal_to = tk.Label(text="is equal to", font=("Arial",24,"bold"))
is_equal_to.grid(column=1,row=2)
km_value = tk.Label(text="0", font=("Arial",24,"bold"))
km_value.grid(column=2, row=2)
KM = tk.Label(text="Km", font=("Arial",24,"bold"))
KM.grid(column=3,row=2)

# Entry
miles = tk.IntVar()
input = tk.Entry(width=10, textvariable=miles)
input.grid(column=2,row=1)

# Button
calculate_button = tk.Button(text="Click Me",bg="grey", fg="blue", command=calculate)
calculate_button.grid(column=2,row=3)

window.mainloop()