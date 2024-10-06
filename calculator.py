from tkinter import *
from tkinter import ttk

class Field:
    def __init__(self, x, y, root):
        self.x = x
        self.y = y
        self.root = root
        self.entry_value = StringVar()

    def extention_button(self, value):
        pass

    def button_click(self, value):
        current_text = self.entry_value.get() if self.entry_value.get() else ""

        if value  == "x":
            value = "*"

        if value in ["C", "=", "+/-", "..."]:
            if value == "C":
                self.entry_value.set("")

            if value == "+/-":
                result = float(current_text) * -1
                self.entry_value.set(result)

            if value == "=":
                try:
                    if "%" in current_text:
                        parts = current_text.split("%")
                        if len(parts) == 2:
                            number = float(parts[0])
                            percent = float(parts[1]) 
                            result = number * percent / 100
                            self.entry_value.set(str(result))
                        return
                    else:
                        result = eval(self.entry_value.get())
                        self.entry_value.set(result)
                
                except:
                    self.entry_value.set("ERROR")

            if value == "...":
                self.create_extentions_buttons(60, 30)

        else:
            current_text = self.entry_value.get()
            self.entry_value.set(current_text + value)

    def create_extentions_buttons(self, resize_x, resize_y):
        buttons = [
            ("sqrt", self.x, self.y + resize_y*6),
            ("^", self.x + resize_x, self.y + resize_y*6)
        ]
        for (text, pos_x, pos_y) in buttons:
            btn = ttk.Button(text=text, command=lambda t=text: self.button_click(t))
            btn.place(x=pos_x, y=pos_y, width=60, height=30)

    def create_buttons(self, resize_x, resize_y):
        buttons = [
            ("9", self.x + resize_x*2, self.y + resize_y),
            ("8", self.x + resize_x, self.y + resize_y),
            ("7", self.x, self.y + resize_y),
            ("6", self.x + resize_x*2, self.y + resize_y*2),
            ("5", self.x + resize_x, self.y + resize_y*2),
            ("4", self.x, self.y + resize_y*2),
            ("3", self.x + resize_x*2, self.y + resize_y*3),
            ("2", self.x + resize_x, self.y + resize_y*3),
            ("1", self.x, self.y + resize_y*3),
            ("0", self.x + resize_x, self.y + resize_y*4),
            (".", self.x + resize_x*2, self.y + resize_y*4),
            ("+/-", self.x, self.y + resize_y*4),
            ("+", self.x + resize_x*3, self.y + resize_y*3),
            ("-", self.x + resize_x*3, self.y + resize_y*2),
            ("=", self.x + resize_x*3, self.y + resize_y*4),
            ("x", self.x + resize_x*3, self.y + resize_y),
            ("C", self.x, self.y),
            ("()", self.x + resize_x, self.y),
            ("%", self.x + resize_x*2, self.y),
            ("/", self.x + resize_x*3, self.y),
        ]

        for (text, pos_x, pos_y) in buttons:
            btn = ttk.Button(text=text, command=lambda t=text: self.button_click(t))
            btn.place(x=pos_x, y=pos_y, width=60, height=30)

        btn_extentions = ttk.Button(text="...")
        btn_extentions.place(x=self.x + resize_x*4, y=self.y + resize_y, width=90, height=90)

    def create_entry(self):
        entry = ttk.Entry(self.root, textvariable=self.entry_value, font=('Arial', 20))
        entry.pack(anchor=N, padx=4, pady=4)

root = Tk()
root.title("Calculator")
root.geometry("350x500")

aField = Field(10, 40, root)
aField.create_entry()
aField.create_buttons(60, 30)

root.mainloop()