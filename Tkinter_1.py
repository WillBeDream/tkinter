import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror
from tkinter import messagebox
from settings import *

app = tkinter.Tk()
app.title(APP_NAME)
app.minsize(width=WIDTH, height = HEIGHT)
app.maxsize(width=WIDTH, height = HEIGHT)

text = tkinter.Text(app, width=WIDTH - 100, height = HEIGHT, wrap = "word")
scroll = Scrollbar(app, orient = VERTICAL, command = text.yview)
scroll.pack(side = "right", fill = "y" )
text.configure(yscrollcommand = scroll.set)
text.pack()

class Text_editor():
    def __init__(self):
        self.file_name = tkinter.NONE

    def new_file(self):
        self.file_name = "Без названия"
        text.delete(1.0, tkinter.END)

    def open_file(self):
        inp = askopenfile(mode = "r")
        if inp is None:
            return
        data = inp.read()
        text.delete(1.0, tkinter.END)
        text.insert(1.0, data) 


    def save_file(self):
        data = text.get(1.0, tkinter.END)
        output = open(self.file_name, "w", encoding="utf-8")
        output.write(data)               
        output.close()

    def save_as_file(self):
        output = asksaveasfile(mode="w",defaultextension="txt")
        data = text.get(1.0, tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка", message="Ошибка при сохранении файла")


    def get_info(self):
        messagebox.showinfo("Справка","Информация о нашем приложении! Спасибо что его используете")





menuBar = tkinter.Menu(app)   

editor = Text_editor()

app_menu = tkinter.Menu(menuBar)
app_menu.add_command(label="Новый",command=editor.new_file)
app_menu.add_command(label="Открыть файл",command=editor.open_file)
app_menu.add_command(label="Сохранить",command=editor.save_file)
app_menu.add_command(label="Сохранить как",command=editor.save_as_file)

app_menu_2 = tkinter.Menu(menuBar)
app_menu_2.add_command(label="Посмотреть справку")
app_menu_2.add_command(label="О программе")

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Справка",command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)
menuBar.add_cascade(label="Формат")


app.config(menu=menuBar)

app.mainloop()