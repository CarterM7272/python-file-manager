import tkinter as tk

app = tk.Tk()

def button_click():
    label.config(text="Python File Manager")

button = tk.Button(app, text="Click me!", command=button_click)
label = tk.Label(app, text="Python File Manager")

label.pack(pady=10)
button.pack(pady=20)

app.mainloop()